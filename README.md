# API Automation Framework

This project provides a robust and scalable API automation framework specifically designed
for the Weatherstack API, built with Python and Pytest. It demonstrates best practices for
designing, implementing, and running automated API tests.

## Important Note on API Key

The Weatherstack API requires an an `access_key`. For security and best practices,
this framework now loads the API key from environment variables, typically via a `.env` file.
You can get the same from https://weatherstack.com/ and paste in `{YOUR_API_KEY}` in `.env` file.

## Note:

Please run `pip install -e .` and `pip install -r requirements.txt` in venv before running the tests.

## Test cases:
|Method|Test case|
|---|---|
|`test_get_current_weather_success`|Verify that all the values corresponding to a city are provided as response when valid city and api_key are provided.|
|`test_get_current_weather_invalid_api_key`|Verify that appropriate error message is provided as response when an invalid api_key is provided.|
|`test_get_current_weather_invalid_query_location`|Verify that appropriate error message is provided as response when an invalid query(location) is provided.|
|`test_get_current_weather_with_units`|Verify that weather details of cities are provided in the requested units in response when the units value is provided.|
|`test_get_current_weather_no_query_parameter`|Verify that appropriate error message is provided as response when an no query(location) is provided.|

## Why This Framework Is Best

This API automation framework is designed with several core principles that make it a highly effective and maintainable solution for API testing:

* **Modularity and Reusability:** The framework follows a clear separation of concerns.
    * **API Client (`api/weatherstack_api.py`):** All API interaction logic is encapsulated here, making it easy to update endpoints or parameters without touching test cases.
    * **Assertion Utilities (`utils/assertions.py`):** Common validation methods (e.g., status code, schema, header, field value checks) are centralized and reusable across all tests and even different APIs.
    * **Schema Definitions (`schemas/weatherstack_schemas.py`):** JSON schemas are kept in dedicated files, ensuring a single source of truth for API response structures and improving readability of test files.
    This modularity drastically reduces code duplication and enhances maintainability.

* **Robust Validation:** Beyond basic status code checks, the framework implements comprehensive response validation:
    * **Status Code Verification:** Ensures correct HTTP status codes are returned.
    * **Payload Schema Validation:** Utilizes `jsonschema` to rigorously assert the structure, data types, and required fields of JSON responses, catching subtle breaking changes quickly.
    * **Header Validation:** Verifies expected HTTP response headers for correctness.
    * **Granular Content Assertions:** Provides flexible assertions (e.g., `assert_json_field_value_contains`) to handle dynamic data and partial matches, reducing test flakiness.

* **Data-Driven Testing with Pytest:** Leverages `pytest.mark.parametrize` extensively to run the same test logic with multiple sets of input data. This approach:
    * **Reduces Code Duplication:** Avoids writing repetitive test functions for similar scenarios.
    * **Increases Test Coverage:** Easily expands test coverage by adding new data points.
    * **Improves Readability:** Test functions remain concise and focused on the core logic.

* **Secure Credential Management:** API keys are managed securely using `.env` files and `dotenv`. This prevents sensitive information from being hardcoded into the codebase or accidentally committed to version control, which is critical for security best practices.

* **Scalability and Maintainability:** The architecture is designed for growth. Adding new API endpoints, new APIs, or expanding test scenarios is straightforward due to the layered and modular design. The emphasis on reusability ensures that the framework remains manageable even as the test suite grows.

* **Problem-Solving Focus:** The framework anticipates common API testing challenges, such as APIs returning `200 OK` with an error payload (as seen with Weatherstack). It includes explicit checks for such scenarios, ensuring accurate test outcomes and preventing misleading "passes."