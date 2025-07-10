from jsonschema import validate, ValidationError

class Assertions:
    """
    Utility class for performing common assertions on API responses.
    """
    @staticmethod
    def assert_status_code(response, expected_code):
        """
        Asserts that the HTTP status code of the response matches the expected code.

        Args:
            response (requests.Response): The response object from the API.
            expected_code (int): The expected HTTP status code.
        """
        print(f"Asserting status code: Expected {expected_code}, Got {response.status_code}")
        assert response.status_code == expected_code, \
            f"Expected status code {expected_code}, but got {response.status_code}. Response: {response.text}"

    @staticmethod
    def validate_json_schema(response_json, schema):
        """
        Validates the JSON response payload against a given JSON schema.

        Args:
            response_json (dict): The JSON payload from the API response.
            schema (dict): The JSON schema to validate against.

        Raises:
            AssertionError: If the JSON payload does not conform to the schema.
        """
        print("Validating JSON schema...")
        try:
            validate(instance=response_json, schema=schema)
            print("JSON schema validation successful.")
        except ValidationError as e:
            raise AssertionError(f"JSON schema validation failed: {e.message} at {e.path}")

    @staticmethod
    def assert_header_value(response, header_name, expected_value):
        """
        Asserts that a specific header in the response has the expected value.

        Args:
            response (requests.Response): The response object from the API.
            header_name (str): The name of the header to check.
            expected_value (str): The expected value of the header.
        """
        print(f"Asserting header '{header_name}': Expected '{expected_value}'")
        assert header_name in response.headers, \
            f"Header '{header_name}' not found in response headers."
        assert response.headers[header_name] == expected_value, \
            f"Header '{header_name}' expected '{expected_value}', but got '{response.headers[header_name]}'."

    @staticmethod
    def assert_json_field_exists(json_data, field_name):
        """
        Asserts that a specific field exists in the JSON data.

        Args:
            json_data (dict): The JSON data to check.
            field_name (str): The name of the field to check for existence.
        """
        print(f"Asserting field '{field_name}' exists in JSON.")
        assert field_name in json_data and json_data[field_name] is not None, f"Field '{field_name}' is missing or None."


    @staticmethod
    def assert_json_field_type(json_data, field_name, expected_type):
        """
        Asserts that a specific field in the JSON data has the expected data type.

        Args:
            json_data (dict): The JSON data to check.
            field_name (str): The name of the field to check.
            expected_type (type): The expected Python data type (e.g., str, int, list).
        """
        print(f"Asserting field '{field_name}' type: Expected {expected_type.__name__}")
        field_data = json_data.get(field_name)
        assert isinstance(field_data, expected_type), \
            f"Field '{field_name}' expected type {expected_type.__name__}, but got {type(field_data).__name__}."

    @staticmethod
    def assert_json_field_value(json_data, field_name, expected_value):
        """
        Asserts that a specific field in the JSON data has the expected value.

        Args:
            json_data (dict): The JSON data to check.
            field_name (str): The name of the field to check.
            expected_value: The expected value of the field.
        """
        print(f"Asserting field '{field_name}' value: Expected '{expected_value}'")
        field_data = json_data.get(field_name)
        assert field_data == expected_value, \
            f"Field '{field_name}' expected value '{expected_value}', but got '{field_data}'."
        
    @staticmethod
    def assert_json_field_value_contains(json_data, field_name, expected_value):
        """
        Asserts that a specific field in the JSON data contains the expected value.

        Args:
            json_data (dict): The JSON data to check.
            field_name (str): The name of the field to check.
            expected_value: The expected value to be contained in the field.
        """
        print(f"Asserting field '{field_name}' contains: Expected '{expected_value}'")
        field_data = json_data.get(field_name)
        assert expected_value in field_data, \
            f"Field '{field_name}' does not contain expected value '{expected_value}'. Actual value: '{field_data}'."