# Swiss Ephemeris API Endpoint (python)

This is a simple python API endpoint for the Swiss Ephemeris library. It is a simple REST API that can be used to get the planetary positions for a given date and time.

## Installation

1. Clone the repository:

```bash
    git clone https://github.com/mohammad-ammad/swiss-Ephemeris-api.git
```

2. Build the Docker image:

```bash
    docker build -t pyswisseph-api .
```

3. Run the Docker container:

```bash
    docker run -p 5000:5000 pyswisseph-api
```

4. Test the API Using CURL:
   Now you have an API running on http://localhost:5000. You can send POST requests to /calculate_chart with JSON data to get astrological calculations.
   To test the API, you can use curl or any API testing tool like Postman. Here's an example using curl:

```bash
    curl -X POST http://localhost:5000/calculate_chart \
     -H "Content-Type: application/json" \
     -d '{"year": 1990, "month": 1, "day": 1, "hour": 12, "minute": 0, "latitude": 40.7128, "longitude": -74.0060}'
```

5. Test the API Using Postman:
   You can also use Postman to test the API. Here's how you can do it:

- Open Postman and create a new request.
- Set the request type to POST.
- Set the request URL to http://localhost:5000/calculate_chart.
- Set the request body to JSON and enter the following data:

```json
{
  "year": 1990,
  "month": 1,
  "day": 1,
  "hour": 12,
  "minute": 0,
  "latitude": 40.7128,
  "longitude": -74.0060
}
``` 

- Click the Send button to make the request.
- You should see the response from the API with the astrological calculations.

