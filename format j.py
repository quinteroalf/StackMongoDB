import json

# Example JSON document
json_document = {
    "name": "Post Name",
    "bedrooms": 3,
    "price": 200000,
    "details": {
        "type": "House",
        "location": "City Center"
    }
}

# Convert JSON document to a formatted string
formatted_json = json.dumps(json_document, indent=2)

# Print the formatted JSON
print(formatted_json)
