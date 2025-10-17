import requests

base_url = "https://archive-api.open-meteo.com/v1/archive?"

def get_hourly_temps(latitude, longitude, date):
    url = (
        f"{base_url}"
        f"latitude={latitude}&longitude={longitude}"
        f"&start_date={date}&end_date={date}"
        f"&hourly=temperature_2m"
        f"&timezone=auto"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temps = data.get("hourly", {})
        print("Success!")
        return temps
    else:
        print(f"Unable to retrieve data: {response.status_code}")
        return None

# Example: Toronto on Aug 1, 2023
hourly_data = get_hourly_temps(43.690685, -79.41174, "2025-10-06")
print(hourly_data)
