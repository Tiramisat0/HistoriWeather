from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from datetime import datetime

from apimanager import get_hourly_temps, get_daily_temps

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

# Max length for hourly ranges (inclusive, in days)
MAX_HOURLY_DAYS = 120  # ~4 months


# ---------- PAGE ROUTES ----------

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/hourly")
def hourly_page():
    # "Hourly (1 day – 4 months)" page
    return send_from_directory(".", "livedata.html")


@app.route("/daily")
def daily_page():
    # "Daily min/max" page
    return send_from_directory(".", "rangeTemp.html")


# ---------- API ROUTES ----------

@app.route("/api/hourly")
def api_hourly():
    """
    Hourly data for ranges between 1 day and MAX_HOURLY_DAYS (inclusive).
    Example:
      /api/hourly?lat=43.7&lon=-79.4&startDate=2024-01-01&endDate=2024-02-15
    """
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)
    start_date = request.args.get("startDate", type=str)
    end_date = request.args.get("endDate", type=str)

    if lat is None or lon is None or not start_date or not end_date:
        return jsonify({"error": "lat, lon, startDate, and endDate are required"}), 400

    # Validate dates and range
    try:
        start_dt = datetime.fromisoformat(start_date)
        end_dt = datetime.fromisoformat(end_date)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    if end_dt < start_dt:
        return jsonify({"error": "endDate must be on or after startDate."}), 400

    span_days = (end_dt - start_dt).days + 1
    if span_days < 1:
        return jsonify({"error": "Range must be at least 1 day."}), 400

    if span_days > MAX_HOURLY_DAYS:
        return jsonify({
            "error": (
                f"Range is {span_days} days, which is longer than the "
                f"maximum {MAX_HOURLY_DAYS} days for hourly data. "
                "Use the Daily High/Low page instead."
            )
        }), 400

    try:
        hourly = get_hourly_temps(lat, lon, start_date, end_date)
    except Exception as e:
        print("Error calling Open-Meteo (hourly):", e)
        return jsonify({"error": "Failed to retrieve data from weather API"}), 502

    if not hourly:
        return jsonify({"error": "No data returned for that date range/location"}), 404

    return jsonify(hourly), 200


@app.route("/api/daily")
def api_daily():
    """
    Daily min/max data for any date range.
    Example:
      /api/daily?lat=43.7&lon=-79.4&startDate=2020-01-01&endDate=2024-12-31
    """
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)
    start_date = request.args.get("startDate", type=str)
    end_date = request.args.get("endDate", type=str)

    if lat is None or lon is None or not start_date or not end_date:
        return jsonify({"error": "lat, lon, startDate, and endDate are required"}), 400

    try:
        start_dt = datetime.fromisoformat(start_date)
        end_dt = datetime.fromisoformat(end_date)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    if end_dt < start_dt:
        return jsonify({"error": "endDate must be on or after startDate."}), 400

    try:
        daily = get_daily_temps(lat, lon, start_date, end_date)
    except Exception as e:
        print("Error calling Open-Meteo (daily):", e)
        return jsonify({"error": "Failed to retrieve data from weather API"}), 502

    if not daily:
        return jsonify({"error": "No data returned for that date range/location"}), 404

    return jsonify(daily), 200


if __name__ == "__main__":
    app.run(debug=True)
