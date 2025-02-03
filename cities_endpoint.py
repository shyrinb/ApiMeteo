from flask import Blueprint, jsonify # type: ignore

cities = Blueprint('cities', __name__)

# Liste des villes fictives (tu peux les modifier)
cities_data = [
    {"name": "Paris", "country": "France", "population": 2148000},
    {"name": "Lyon", "country": "France", "population": 515695},
    {"name": "Marseille", "country": "France", "population": 861635},
    {"name": "Toulouse", "country": "France", "population": 479553},
    {"name": "Nice", "country": "France", "population": 342637}
]

@cities.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(cities_data)
