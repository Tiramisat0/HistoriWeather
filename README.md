# HistoriWeather  
**HistoriWeather** is a simple web app which lets you easily browse historical weather data and archives anywhere in the world. 


## Features
Easily look up **hourly temperature data** 

Just enter:
- Latitude  
- Longitude  
- Date  

and the app fetches real data from the **Open-Meteo Archive API**, then displays an **interactive line chart** and a **scrollable data table**  

It’s lightweight, fast, and requires no API keys.



**Future features/ideas:** 
- Multi-day Charts
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
- **Open-Meteo Archive API** - A Free API with no key required. Has global coverage and 


