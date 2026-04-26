import requests

api_key = '123456789' # Replace with your actual API key. Please contact the author of the API (shilianz@ifi.uio.no) to request a valid API key with your institutional email address
latitude = 47.3902015 # An example of the location you are interested in
longitude = 8.5193411

BASE_URL = "https://geosolar-production.up.railway.app" # This is where we deployed our API, please do not change it
api_endpoint_url = f"{BASE_URL}/{api_key}/{latitude}/{longitude}"  # Construct the full API endpoint URL


# Fetch Data from our API
print(f"Fetching data from: {api_endpoint_url}")
try:
    response = requests.get(api_endpoint_url)
    response.raise_for_status() # Check for 4xx/5xx errors

    html = response.text
    # Below we save the response data to a file and open in a browser
    with open("map.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Saved map.html")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    # Exit or handle the error gracefully
    exit()
