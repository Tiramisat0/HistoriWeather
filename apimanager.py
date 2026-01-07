import requests

BASE_URL = "https://archive-api.open-meteo.com/v1/archive"


def get_hourly_temps(latitude, longitude, startDate, endDate):
    """
    Fetch hourly 2m temperature data between startDate and endDate (inclusive).
    Returns a dict like {"time": [...], "temperature_2m": [...]}.
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": startDate,
        "end_date": endDate,
        "hourly": "temperature_2m",
        "timezone": "auto",
    }

    resp = requests.get(BASE_URL, params=params, timeout=10)

    if resp.status_code != 200:
        raise RuntimeError(f"Weather API error: {resp.status_code} {resp.text[:200]}")

    data = resp.json()
    return data.get("hourly", {})


def get_daily_temps(latitude, longitude, startDate, endDate):
    """
    Fetch DAILY aggregated temperature data (min, max) between startDate and endDate (inclusive).
    Returns a dict like:
      {
        "time": [...],
        "temperature_2m_min": [...],
        "temperature_2m_max": [...]
      }
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": startDate,
        "end_date": endDate,
        "daily": "temperature_2m_min,temperature_2m_max",
        "timezone": "auto",
    }

    resp = requests.get(BASE_URL, params=params, timeout=10)

    if resp.status_code != 200:
        raise RuntimeError(f"Weather API error: {resp.status_code} {resp.text[:200]}")

    data = resp.json()
    return data.get("daily", {})
