# Geosolar

We release an API named Geosolar. Particularly, for any user‑specified building location, our API automatically retrieves the corresponding satellite imagery from open-source aerial imagery sources, detects rooftop solar panels, and returns georeferenced panel polygons that can be directly used in maps and programming works.

We show an example of solar panel detection for a single building in the city of Zurich in Switzerland in [this html file](https://github.com/slzhang-git/GeoSolarDataAI/blob/main/example_Zurich.html), where we store all the geographic geometry of the detected panels at line 138 of the file. The visualization of the detected solar panels is below, and we also show the detected panel in an [interactive map](https://slzhang-git.github.io/GeoSolarDataAI/example_Zurich.html).

<img width="1378" height="1067" alt="example" src="https://github.com/user-attachments/assets/7ea129ba-98c3-49d7-9ae2-831c698558b0" />

<br><br/>

**Below is a python programming example for using our API in Google Colab environment:**

```python
import requests

api_key = '123456789' # Replace with your actual API key. Please contact the author of the API (shiliangz@ieee.org) to request a valid API key with your institutional email address
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
```
