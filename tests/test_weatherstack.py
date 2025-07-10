import pytest
from api.weatherstack_api import WeatherstackAPI
from utils.assertions import Assertions
from config.settings import Settings
from schemas.weatherstack_schemas import WeatherstackSchemas

@pytest.fixture(scope="module")
def weatherstack_api_client():
    """
    Pytest fixture to provide a single instance of WeatherstackAPI for all tests in the module.
    """
    return WeatherstackAPI()

class TestWeatherstackAPI:
    """
    Test suite for the Weatherstack API.
    """
    @pytest.mark.parametrize("query_location", ["New Delhi", "New York", "London"])
    def test_get_current_weather_success(self, weatherstack_api_client, query_location):
        """
        Verify that all the values corresponding to a city are provided as response when valid city and api_key are provided.
        """
        response = weatherstack_api_client.get_current_weather(query=query_location)

        # 1. Status Code Verification
        Assertions.assert_status_code(response, 200)

        # 2. Header Validation
        Assertions.assert_header_value(response, "Content-Type", "application/json; Charset=UTF-8")

        # 3. Payload Validation
        response_json = response.json()

        Assertions.validate_json_schema(response_json, WeatherstackSchemas.CURRENT_WEATHER_SCHEMA)

        # Further content validation
        Assertions.assert_json_field_value_contains(response_json["request"], "query", query_location)
        Assertions.assert_json_field_exists(response_json["location"], "name")
        Assertions.assert_json_field_value(response_json["location"], "name", query_location)
        Assertions.assert_json_field_type(response_json["current"], "temperature", int)
        assert response_json["current"]["temperature"] is not None, "Temperature should not be None."

    def test_get_current_weather_invalid_api_key(self, weatherstack_api_client):
        """
        Verify that appropriate error message is provided as response when an invalid api_key is provided.
        """
        original_api_key = weatherstack_api_client.api_key
        weatherstack_api_client.api_key = "invalid_key_123"

        try:
            query = "New York"
            response = weatherstack_api_client.get_current_weather(query=query)

            # Weatherstack returns 200 OK even for invalid keys, but includes an error object.
            Assertions.assert_status_code(response, 200)
            Assertions.assert_header_value(response, "Content-Type", "application/json; Charset=UTF-8")

            response_json = response.json()

            # Validate against the error response schema
            Assertions.validate_json_schema(response_json, WeatherstackSchemas.ERROR_RESPONSE_SCHEMA)

            # Assert specific error details
            Assertions.assert_json_field_value(response_json, "success", False)
            Assertions.assert_json_field_value(response_json["error"], "code", 101)
            Assertions.assert_json_field_value(response_json["error"], "type", "invalid_access_key")
            Assertions.assert_json_field_exists(response_json["error"], "info")
            Assertions.assert_json_field_value_contains(response_json["error"], "info", "You have not supplied a valid API Access Key.")

        finally:
            # Restore the original API key
            weatherstack_api_client.api_key = original_api_key

    @pytest.mark.parametrize("query_location", ["NonExistentCity12345", "InvalidQuery@#$"])
    def test_get_current_weather_invalid_query_location(self, weatherstack_api_client, query_location):
        """
        Verify that appropriate error message is provided as response when an invalid query(location) is provided.
        """
        response = weatherstack_api_client.get_current_weather(query=query_location)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_header_value(response, "Content-Type", "application/json; Charset=UTF-8")

        response_json = response.json()

        # Validate against the error response schema
        Assertions.validate_json_schema(response_json, WeatherstackSchemas.ERROR_RESPONSE_SCHEMA)

        # Assert specific error details
        Assertions.assert_json_field_value(response_json, "success", False)
        Assertions.assert_json_field_value(response_json["error"], "code", 615)
        Assertions.assert_json_field_value(response_json["error"], "type", "request_failed")
        Assertions.assert_json_field_exists(response_json["error"], "info")
        Assertions.assert_json_field_value_contains(response_json["error"], "info", "Your API request failed. Please try again or contact support.")


    @pytest.mark.parametrize("query, units", [
        ("Paris", "m"),
        ("Tokyo", "f"),
        ("Berlin", "s")
    ])
    def test_get_current_weather_with_units(self, weatherstack_api_client, query, units):
        """
        Verify that weather details of cities are provided in the requested units in response when the units value is provided.
        """
        response = weatherstack_api_client.get_current_weather(query=query, units=units)

        Assertions.assert_status_code(response, 200)
        Assertions.assert_header_value(response, "Content-Type", "application/json; Charset=UTF-8")

        response_json = response.json()

        # Verify the unit in the response
        Assertions.assert_json_field_value(response_json["request"], "unit", units)
        Assertions.assert_json_field_exists(response_json["current"], "temperature")
        Assertions.assert_json_field_type(response_json["current"], "temperature", int)


    def test_get_current_weather_no_query_parameter(self, weatherstack_api_client):
        """
        Verify that appropriate error message is provided as response when an no query(location) is provided.
        """
        # Make a request without the 'query' parameter (or with an empty string)
        response = weatherstack_api_client.get_current_weather(query="")

        Assertions.assert_status_code(response, 200)
        Assertions.assert_header_value(response, "Content-Type", "application/json; Charset=UTF-8")

        response_json = response.json()

        # Verify the error response
        Assertions.validate_json_schema(response_json, WeatherstackSchemas.ERROR_RESPONSE_SCHEMA)
        Assertions.assert_json_field_value(response_json, "success", False)
        Assertions.assert_json_field_value(response_json["error"], "code", 601)
        Assertions.assert_json_field_value(response_json["error"], "type", "missing_query")
        Assertions.assert_json_field_exists(response_json["error"], "info")
        Assertions.assert_json_field_value_contains(response_json["error"], "info", "Please specify a valid location identifier using the query parameter.")