import json
import jsonschema
from jsonschema import validate

# Define the schema for structure validation
schema = {
    "type": "object",
    "properties": {
        "instances": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "serving_default_inputs:0": {
                        "type": "array",
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "array",
                                "items": {
                                    "type": "array",
                                    "items": {
                                        "type": "number"
                                    },
                                    "minItems": 3,
                                    "maxItems": 3
                                },
                                "minItems": 160,
                                "maxItems": 160
                            },
                            "minItems": 160,
                            "maxItems": 160
                        },
                        "minItems": 1
                    }
                },
                "required": ["serving_default_inputs:0"]
            }
        }
    },
    "required": ["instances"]
}

def validate_json(payload):
    try:
        validate(instance=payload, schema=schema)
        print("JSON payload is valid.")
    except jsonschema.exceptions.ValidationError as e:
        print(f"JSON payload is invalid: {e.message}")

def check_data_types(payload):
    try:
        instances = payload['instances']
        for instance in instances:
            inputs = instance['serving_default_inputs:0']
            for img in inputs:
                if not all(isinstance(row, list) for row in img):
                    raise ValueError("Image data rows are not lists.")
                for row in img:
                    if not all(isinstance(pixel, list) for pixel in row):
                        raise ValueError("Row pixels are not lists.")
                    for pixel in row:
                        if not all(isinstance(value, float) for value in pixel):
                            raise ValueError("Pixel values are not floats.")
        print("Data types and formats are correct.")
    except Exception as e:
        print(f"Data types and formats are incorrect: {e}")

def check_field_names(payload):
    expected_field_name = "serving_default_inputs:0"
    try:
        instances = payload['instances']
        for instance in instances:
            if expected_field_name not in instance:
                raise ValueError(f"Expected field '{expected_field_name}' not found.")
        print("Field names are correct.")
    except Exception as e:
        print(f"Field names are incorrect: {e}")

# Example payload to test with smaller data
payload = {
    "instances": [
        {
            "serving_default_inputs:0": [
                [[[0.0] * 3] * 160] * 160  # Replace with smaller data if necessary
            ]
        }
    ]
}

validate_json(payload)
check_data_types(payload)
check_field_names(payload)
