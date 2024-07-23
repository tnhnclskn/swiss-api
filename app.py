from flask import Flask, request, jsonify
import swisseph as swe

app = Flask(__name__)

@app.route('/calculate_chart', methods=['POST'])
def calculate_chart():
    data = request.json
    year = data['year']
    month = data['month']
    day = data['day']
    hour = data['hour']
    minute = data['minute']
    latitude = data['latitude']
    longitude = data['longitude']

    t = swe.utc_to_jd(year, month, day, hour, minute, 0, swe.GREG_CAL)[1]

    sun = swe.calc_ut(t, swe.SUN)[0]
    moon = swe.calc_ut(t, swe.MOON)[0]

    houses = swe.houses(t, latitude, longitude)[0]

    result = {
        'julian_day': t,
        'sun_longitude': sun[0],
        'moon_longitude': moon[0],
        'ascendant': houses[0]
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')