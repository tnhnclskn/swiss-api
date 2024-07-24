# Swiss Ephemeris API

This is a simple Python API endpoint for the Swiss Ephemeris library. It is a REST API that provides planetary positions for a given date and time.

## Installation Using Docker

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mohammad-ammad/swiss-Ephemeris-api.git
   ```

2. **Build the Docker image:**

   ```bash
   sudo docker build -t pyswisseph-api .
   ```

3. **Run the Docker container:**

   ```bash
   sudo docker run -p 5000:5000 pyswisseph-api
   ```

## Installation Without Docker

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mohammad-ammad/swiss-Ephemeris-api.git
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API:**

   ```bash
   python app.py
   ```

## Testing the API

Now you have an API running on `http://localhost:5000`. You can send POST requests to `/calculate_chart` with JSON data to get astrological calculations.

### Using CURL

```bash
curl -X POST http://localhost:5000/calculate_chart \
 -H "Content-Type: application/json" \
 -d '{
  "name": "John Doe",
  "place_of_birth": "New York, USA",
  "dob": "18/06/1998",
  "time": "14:30"
}'
```

### Using Postman

1.  Open Postman and create a new request.

2.  Set the request type to POST.

3.  Set the request URL to http://localhost:5000/calculate_chart.

4.  Set the request body to JSON and enter the following data:

```json
{
  "name": "John Doe",
  "place_of_birth": "New York, USA",
  "dob": "18/06/1998",
  "time": "14:30" // optional
}
```

5. Click the Send button to make the request.

6. You should see the response from the API with the astrological calculations.
