from flask import Flask, request, jsonify
from flask_cors import CORS
import swisseph as swe
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes
geolocator = Nominatim(user_agent="my_astrology_app")

def get_zodiac_sign(longitude):
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    sign_index = int(longitude / 30)
    return signs[sign_index]

def get_coordinates(place):
    try:
        location = geolocator.geocode(place)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except (GeocoderTimedOut, GeocoderUnavailable):
        return None, None

def calculate_planet_position(jd, planet):
    return swe.calc_ut(jd, planet)[0]

@app.route('/calculate_chart', methods=['POST'])
def calculate_chart():
    data = request.json
    place_of_birth = data.get('place_of_birth', None)
    latitude = data.get('latitude', None)
    longitude = data.get('longitude', None)
    dob = data['dob']  # Expected format: "DD/MM/YYYY"
    time = data.get('time', '00:00')  # Optional, default to midnight if not provided

    # Get coordinates from place of birth
    if not place_of_birth and (latitude is None or longitude is None):
        return jsonify({"error": "Place of birth or coordinates must be provided"}), 400
    if place_of_birth:
        latitude, longitude = get_coordinates(place_of_birth)
        if latitude is None or longitude is None:
            return jsonify({"error": "Unable to geocode the place of birth"}), 400
    if latitude is None or longitude is None:
        return jsonify({"error": "Invalid coordinates"}), 400

    # Parse date and time
    dob_obj = datetime.strptime(dob, "%d/%m/%Y")
    time_obj = datetime.strptime(time, "%H:%M")
    
    year = dob_obj.year
    month = dob_obj.month
    day = dob_obj.day
    hour = time_obj.hour
    minute = time_obj.minute
    
    jd = swe.utc_to_jd(year, month, day, hour, minute, 0, swe.GREG_CAL)[1]
    
    # Calculate houses first
    houses = swe.houses(jd, latitude, longitude)[0]
    ascendant = houses[0]

    # Calculate positions for all planets
    planets = {
        'Sun': swe.SUN,
        'Moon': swe.MOON,
        'Mercury': swe.MERCURY,
        'Venus': swe.VENUS,
        'Mars': swe.MARS,
        'Jupiter': swe.JUPITER,
        'Saturn': swe.SATURN,
        'Uranus': swe.URANUS,
        'Neptune': swe.NEPTUNE,
        'Pluto': swe.PLUTO,
        'Ascendant': swe.ASC 
    }

    planet_positions = {}
    for planet_name, planet_id in planets.items():
        if planet_name == 'Ascendant':
            xlongitude = ascendant  # Use the previously calculated ascendant
        else:
            xlongitude = calculate_planet_position(jd, planet_id)[0]
        planet_positions[planet_name] = {
            'longitude': xlongitude,
            'sign': get_zodiac_sign(xlongitude)
        }

    result = {
        'latitude': latitude,
        'longitude': longitude,
        'date_of_birth': dob,
        'time_of_birth': time,
        'julian_day': jd,
        'planets': planet_positions,
        'ascendant': {
            'longitude': ascendant,
            'sign': get_zodiac_sign(ascendant)
        },
        'houses': houses
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)