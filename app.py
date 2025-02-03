from flask import Flask # type: ignore
from weather_endpoint import weather # type: ignore
from forecast_endpoint import forecast # type: ignore
from air_quality_endpoint import air_quality # type: ignore
from current_weather_endpoint import current_weather # type: ignore
from cities_endpoint import cities

app = Flask(__name__)

API_KEY = "ac2e6840732ee6b52640142d835863af"
OPENWEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

# Registre des endpoints
app.register_blueprint(weather)
app.register_blueprint(forecast)
app.register_blueprint(air_quality)
app.register_blueprint(current_weather)
app.register_blueprint(cities)

@app.route('/')
def index():
    return "Bienvenue sur l'API Météo!"

if __name__ == '__main__':
    app.run(debug=True)