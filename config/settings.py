import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Configuration settings for the Weatherstack API automation framework.
    """
    BASE_URL = os.getenv("BASE_URL")
    API_KEY = os.getenv("WEATHERSTACK_API_KEY")