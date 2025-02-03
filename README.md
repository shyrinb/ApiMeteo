# ApiMeteo
# Projet API Publique

## Description
Ce projet consiste à créer une API qui consomme une API publique OpenWeatherMap et crée des endpoints pour récupérer des données. Chaque membre de l'équipe travaillera sur une fonctionnalité spécifique et soumettra des pull requests pour intégrer les modifications.

## Langage de programmation et framework
- **Langage** : Python (Flask) *(ou tout autre langage choisi par l'équipe)*
- **Framework** : Flask *(ou tout autre framework choisi par l'équipe)*

## Installer les dependances:
pip install flask requests

## Endpoints
1. **GET /weather** : Renvoie la météo pour une ville donnée.
2. **GET /air_quality** : Renvoie les nouvelles sur la qualité de l'air.
3. **GET /cities** : Renvoie des informations sur la liste des villes données.
4. **GET /forecast** : Renvoie des prévisions meteos.
5. **GET /current** : Renvoie la méteo actuelle.
   
## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/VOTRE-UTILISATEUR/nom-du-repository.git
  ```

## Repartition du travail
  ```bash/weather-api
    ├── app.py                   # Fichier principal pour exécuter le serveur Flask
    ├── weather_endpoint.py      # Endpoint pour la météo d'une ville
    ├── forecast_endpoint.py     # Endpoint pour les prévisions météo
    ├── air_quality_endpoint.py  # Endpoint pour la qualité de l'air
    ├── current_weather_endpoint.py # Endpoint pour la météo actuelle
    └── cities_endpoint.py       # Endpoint pour la liste des villes disponibles
  ```
