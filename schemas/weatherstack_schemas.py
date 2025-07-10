class WeatherstackSchemas:
    """
    Collection of JSON schemas for validating Weatherstack API responses.
    """
    CURRENT_WEATHER_SCHEMA = {
        "type": "object",
        "properties": {
            "request": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "query": {"type": "string"},
                    "language": {"type": "string"},
                    "unit": {"type": "string"}
                },
                "required": ["type", "query", "language", "unit"],
                "additionalProperties": False
            },
            "location": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "country": {"type": "string"},
                    "region": {"type": "string"},
                    "lat": {"type": "string"},
                    "lon": {"type": "string"},
                    "timezone_id": {"type": "string"},
                    "localtime": {"type": "string"},
                    "localtime_epoch": {"type": "integer"},
                    "utc_offset": {"type": "string"}
                },
                "required": ["name", "country", "region", "lat", "lon", "timezone_id", "localtime", "localtime_epoch", "utc_offset"],
                "additionalProperties": False
            },
            "current": {
                "type": "object",
                "properties": {
                    "observation_time": {"type": "string"},
                    "temperature": {"type": "integer"},
                    "weather_code": {"type": "integer"},
                    "weather_icons": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "weather_descriptions": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "astro": {
                        "type": "object",
                        "properties": {
                            "sunrise": {"type": "string"},
                            "sunset": {"type": "string"},
                            "moonrise": {"type": "string"},
                            "moonset": {"type": "string"},
                            "moon_phase": {"type": "string"},
                            "moon_illumination": {"type": "integer"}
                        },
                        "required": [
                            "sunrise", "sunset", "moonrise", "moonset",
                            "moon_phase", "moon_illumination"
                        ],
                        "additionalProperties": False
                    },
                    "air_quality": {
                        "type": "object",
                        "properties": {
                            "co": {"type": "string"},
                            "no2": {"type": "string"},
                            "o3": {"type": "string"},
                            "so2": {"type": "string"},
                            "pm2_5": {"type": "string"},
                            "pm10": {"type": "string"},
                            "us-epa-index": {"type": "string"},
                            "gb-defra-index": {"type": "string"}
                        },
                        "required": [
                            "co", "no2", "o3", "so2", "pm2_5", "pm10",
                            "us-epa-index", "gb-defra-index"
                        ],
                        "additionalProperties": False
                    },
                    "wind_speed": {"type": "integer"},
                    "wind_degree": {"type": "integer"},
                    "wind_dir": {"type": "string"},
                    "pressure": {"type": "integer"},
                    "precip": {"type": "number"},
                    "humidity": {"type": "integer"},
                    "cloudcover": {"type": "integer"},
                    "feelslike": {"type": "integer"},
                    "uv_index": {"type": "integer"},
                    "visibility": {"type": "integer"},
                    "is_day": {"type": "string"}
                },
                "required": [
                    "observation_time", "temperature", "weather_code", "weather_icons",
                    "weather_descriptions", "wind_speed", "wind_degree", "wind_dir",
                    "pressure", "precip", "humidity", "cloudcover", "feelslike",
                    "uv_index", "visibility", "is_day",
                    "astro", "air_quality"
                ],
                "additionalProperties": False
            }
        },
        "required": ["request", "location", "current"],
        "additionalProperties": False
    }

    ERROR_RESPONSE_SCHEMA = {
        "type": "object",
        "properties": {
            "success": {"type": "boolean"},
            "error": {
                "type": "object",
                "properties": {
                    "code": {"type": "integer"},
                    "type": {"type": "string"},
                    "info": {"type": "string"}
                },
                "required": ["code", "type", "info"],
                "additionalProperties": False
            }
        },
        "required": ["success", "error"],
        "additionalProperties": False
    }
