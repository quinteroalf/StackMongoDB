import requests

url = 'https://us-west-2.aws.data.mongodb-api.com/app/data-usgnw/endpoint/data/v1/action/findOne'

headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'e7vZtxFYIGAeS6uJGdqrkUsVbwLF9qCSiGENtIF1FLXLeD8vYZOVQ85kzUGfo03y',
}

data = {
    "dataSource": "CLDW",
    "database": "sample_mflix",
    "collection": "movies",
    "projection": {"title": 1}
}

response = requests.post(url, json=data, headers=headers)

# Print the response
print(response.json())
