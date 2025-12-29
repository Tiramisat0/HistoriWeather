from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from apimanager import get_hourly_temps

# Serve static files (HTML) from the current directory
app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)


@app.route("/")
def home():
    # Serve the main HistoriWeather page
    return send_from_directory(".", "livedata.html")


@app.route("/api/hourly")
def api_hourly():
    """
    Example:
        /api/hourly?lat=43.7&lon=-79.4&date=2025-10-06
    """
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)
    date = request.args.get("date", type=str)

    if lat is None or lon is None or not date:
        return jsonify({"error": "lat, lon, and date are required"}), 400

    try:
        hourly = get_hourly_temps(lat, lon, date)
    except Exception as e:
        print("Error calling Open-Meteo:", e)
        return jsonify({"error": "Failed to retrieve data from weather API"}), 502

    if not hourly:
        return jsonify({"error": "No data returned for that date/location"}), 404

    # hourly is like: { "time": [...], "temperature_2m": [...] }
    return jsonify(hourly), 200


if __name__ == "__main__":
    # Run: python app.py
    app.run(debug=True)
