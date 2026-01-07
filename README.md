# HistoriWeather  
**HistoriWeather** is a simple web app which lets you easily browse historical weather data and archives anywhere in the world. 

## How to Run

### 1. Install dependencies 
   *Make sure you have Python 3
   ```bash
   pip install flask flask-cors requests
   ```
   
### 2. Run Backend
   ```bash
   python app.py
   ```

   You should see: 
   ```
   Running on http://127.0.0.1:5000/
   ```
### 3. Open the app in your browser
   ```
   http://127.0.0.1:5000/
   ```


## Features
Easily look up **Historical Temperature data** with hourly temps for short ranges, 
as well as daily Min/Max for longer ranges. 

Just enter:
- Latitude  
- Longitude  
- Start Date
- End Date 

and the app fetches real data from the **Open-Meteo Archive API**, then displays an **interactive line chart** and a **scrollable data table**  

It’s lightweight, fast, and requires no API keys.



**Future features/ideas:** 
- More products: precipitation, wind, humidity, etc.
- Location by City Name/Map
- Export CSV/other data types
- Selectable Weather API Provider (NOAA, Copernicus/ERA5, etc)

---

## Tech Stack

### Backend
- **Python 3**
- **Flask** — serves the app + API route
- **Requests** — calls Open-Meteo API
- **Flask-CORS** — allows frontend requests

### Frontend
- **HTML + TailwindCSS**
- **Chart.js** — charts hourly temperatures

### Data Source
- **Open-Meteo Archive API** - A Free API with no key required. 


