import requests
from config.settings import Settings

class WeatherstackAPI:
    """
    API client for interacting with the Weatherstack API.
    Encapsulates HTTP requests to different endpoints.
    """
    def __init__(self):
        """
        Initializes the WeatherstackAPI client with the base URL and API key.
        """
        self.base_url = Settings.BASE_URL
        self.api_key = Settings.API_KEY

    def get_current_weather(self, query, units=None, language=None):
        """
        Sends a GET request to the /current endpoint to retrieve current weather data.

        Args:
            query (str): The location (city name, zip code, IP address) for which to retrieve weather data.
            units (str, optional): Units for temperature (m=metric, s=scientific, f=fahrenheit). Defaults to None (metric).
            language (str, optional): Language for the response (e.g., en, de, fr). Defaults to None (English).

        Returns:
            requests.Response: The response object from the API.
        """
        endpoint = f"{self.base_url}current"
        params = {
            'access_key': self.api_key,
            'query': query
        }
        if units:
            params['units'] = units
        if language:
            params['language'] = language

        print(f"Making GET request to: {endpoint} with params: {params}")
        response = requests.get(endpoint, params=params)
        return response