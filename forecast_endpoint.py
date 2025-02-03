from flask import Blueprint, request, jsonify
import requests
import os

# Définir un Blueprint Flask pour ce module
forecast_bp = Blueprint('forecast', __name__)

# Clé API OpenWeatherMap (remplace avec la tienne)
API_KEY = os.getenv("OPENWEATHER_API_KEY", "TA_CLE_API_ICI")
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

@forecast_bp.route('/forecast', methods=['GET'])
def get_forecast():
    """Endpoint pour obtenir les prévisions météo sur 5 jours."""
    city = request.args.get('city')

    if not city:
        return jsonify({"error": "Le paramètre 'city' est requis"}), 400

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",  # Température en degrés Celsius
        "cnt": 5  # Nombre de prévisions (5 jours par défaut)
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            return jsonify({"error": data.get("message", "Erreur inconnue")}), response.status_code

        # Formatage des données
        forecast_list = []
        for forecast in data['list']:
            forecast_list.append({
                "date": forecast["dt_txt"],
                "temperature": forecast["main"]["temp"],
                "description": forecast["weather"][0]["description"],
                "humidity": forecast["main"]["humidity"],
                "wind_speed": forecast["wind"]["speed"]
            })

        return jsonify({
            "city": data["city"]["name"],
            "country": data["city"]["country"],
            "forecasts": forecast_list
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
gi