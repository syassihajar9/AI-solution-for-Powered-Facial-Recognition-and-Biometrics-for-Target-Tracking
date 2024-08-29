import json
import numpy as np

def validate_json_payload(payload):
    try:
        data = json.loads(payload)
    except json.JSONDecodeError as e:
        return f"JSON decoding error: {e}"
    
    if "instances" not in data or not isinstance(data["instances"], list):
        return "Invalid payload format: 'instances' field is missing or not a list."

    if len(data["instances"]) != 1:
        return "Invalid payload format: Expected one instance."

    inputs = data["instances"][0].get("inputs", None)
    if inputs is None:
        return "Invalid payload format: 'inputs' field is missing."

    if not isinstance(inputs, list):
        return "Invalid payload format: 'inputs' should be a list."

    np_inputs = np.array(inputs)
    expected_shape = (1, 160, 160, 3)
    if np_inputs.shape != expected_shape:
        return f"Inputs shape is incorrect. Expected shape: {expected_shape}."

    return "JSON payload is valid."

# Test the validation script
test_payload = {
    "instances": [
        {
            "inputs": [[[[0.0 for _ in range(3)] for _ in range(160)] for _ in range(160)]]
        }
    ]
}

# Convert the test payload to a JSON string
payload_json = json.dumps(test_payload)

# Validate the JSON payload
result = validate_json_payload(payload_json)
print(result)
