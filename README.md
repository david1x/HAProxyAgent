## Example for JSON Output 
```json
// All Mandatory fields
{
    "type": "Resource Monitor", 
    "is_passed": false, 
    "if_failed": { 
        "Reason": {
            "cpu": "Usage over the threshold [ 80% ]"
        }
    },
    "result": {
        "cpu": "Usage over the threshold [ 6% ]",
        "disk": "Usage over the threshold [ 21% ]",
        "memory": "Usage over the threshold [ 3% ]"
    } 
}
```