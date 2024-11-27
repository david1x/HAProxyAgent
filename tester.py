import json
import logging

def is_pass(parameters):
    """Runs tests based on the 'is_passed' field in the JSON parameters."""
    if "is_passed" not in parameters:
        logging.error("JSON file is not using the correct syntax.")
        print("Error: JSON file is not using the correct syntax.")
        return

    if parameters["is_passed"]:
        report = json.dumps(parameters, indent=4)
        logging.info(f"PASS: {report}")
        print(f"PASS: {report}")
        return f"PASS: details in the log file"
        
    else:
        if_failed = parameters.get("if_failed", {})
        test_type = parameters.get("type", "Unknown")
        value = if_failed.get("Reason", {})
        reason = json.dumps(value, indent=4)
        logging.error(f"{test_type} Test FAILED: \nReason: {reason}")
        print(f"{test_type} Test FAILED: \nReason: {reason}")