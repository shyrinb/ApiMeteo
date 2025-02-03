from flask import Blueprint, request, jsonify
import requests
 
weather = Blueprint('weather', __name__)
 
API_KEY = "VOTRE_CLÉ_API_OPENWEATHER"
OPENWEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
 
@weather.route('/weather', methods=['GET'])
def get_weather():
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
        weather_info = {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return jsonify(weather_info)
    return jsonify({"error": "Ville non trouvée ou problème avec l'API"}), 404