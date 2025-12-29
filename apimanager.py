import requests

BASE_URL = "https://archive-api.open-meteo.com/v1/archive"


def get_hourly_temps(latitude, longitude, date):
    """
    Fetch hourly 2m temperature data for a single date.
    Returns a dict like {"time": [...], "temperature_2m": [...]}.
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": date,
        "end_date": date,
        "hourly": "temperature_2m",
        "timezone": "auto",
    }

    resp = requests.get(BASE_URL, params=params, timeout=10)

    if resp.status_code != 200:
        # Let the caller handle this
        raise RuntimeError(f"Weather API error: {resp.status_code} {resp.text[:200]}")

    data = resp.json()
    return data.get("hourly", {})
