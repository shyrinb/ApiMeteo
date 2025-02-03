import requests

def get_air_quality_weatherapi(api_key, location):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=yes"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_air_quality_openweathermap(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

if __name__ == "__main__":
    API_KEY = "ac2e6840732ee6b52640142d835863af"
    LOCATION = "Paris"
    LAT, LON = 48.8566, 2.3522
    
    print("Air Quality from WeatherAPI:")
    print(get_air_quality_weatherapi(API_KEY, LOCATION))
    
    print("\nAir Quality from OpenWeatherMap:")
    print(get_air_quality_openweathermap(API_KEY, LAT, LON))
