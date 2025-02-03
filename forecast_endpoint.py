from flask import Blueprint, request, jsonify
import requests
import os


forecast_bp = Blueprint('forecast', __name__)


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
        "units": "metric",  # Pour afficher la température en Celsius
        "lang": "fr"        # Langue des descriptions météo
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return jsonify({"error": "Ville introuvable ou problème avec l'API"}), response.status_code

    data = response.json()

    # Extraire les prévisions météo (ex : pour 5 jours, toutes les 3 heures)
    forecasts = []
    for forecast in data["list"]:
        forecasts.append({
            "datetime": forecast["dt_txt"],
            "temperature": forecast["main"]["temp"],
            "description": forecast["weather"][0]["description"],
            "humidity": forecast["main"]["humidity"],
            "wind_speed": forecast["wind"]["speed"]
        })

    return jsonify({
        "city": city,
        "forecasts": forecasts
    })
