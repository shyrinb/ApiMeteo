from flask import Blueprint, request, jsonify
import requests
from config import API_KEY, OPENWEATHER_URL

current_weather = Blueprint('current_weather', __name__)

@current_weather.route('/current', methods=['GET'])
def get_current_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "La ville est requise"}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'fr'
    }

    response = requests.get(OPENWEATHER_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        detailed_info = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'pressure': data['main']['pressure'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'wind_deg': data['wind']['deg'],
            'weather_description': data['weather'][0]['description']
        }
        return jsonify(detailed_info)
    return jsonify({"error": "Ville non trouvée ou problème avec l'API"}), 404
