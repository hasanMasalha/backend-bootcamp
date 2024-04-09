import requests
from requests.exceptions import JSONDecodeError

# Replace 'your_api_endpoint' with the actual API endpoint URL
api_endpoint = 'https://api.nasa.gov/'

# Replace 'your_api_key' with your actual API key
api_key = '6E62zwcwRgo7b1xrbPFSwhL1bUZmi4W1HQI24ZL6'

# Define headers with the API key
headers = {'Authorization': f'Bearer {api_key}'}

# Make a GET request to the API with headers
response = requests.get(api_endpoint, headers=headers)

try:
    # Try to parse the JSON data in the response
    api_data = response.json()

    # Now you can work with the data obtained from the API
    print(api_data)

except JSONDecodeError as e:
    print(f"Failed to parse JSON. Error: {e}")
