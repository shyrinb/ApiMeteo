from flask import Flask
from weather_endpoint import weather
from forecast_endpoint import forecast
from air_quality_endpoint import air_quality
from current_weather_endpoint import current_weather
from cities_endpoint import cities

app = Flask(__name__)

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