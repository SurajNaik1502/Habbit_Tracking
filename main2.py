import requests

USERNAME = "suru"
TOKEN = "fbksdjhbvfedbvienb324h4iefd"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

# User Parameters
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Graph Endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",  # Unit label, not related to the quantity value
    "type": "float",  # Must match the format of quantity
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Pixel Creation Endpoint
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Ensure the quantity is a valid float formatted as a string
pixel_data = {
    "date": "20250104",  # Correctly formatted date (YYYYMMDD)
    "quantity": "9.74",  # Valid float as a string
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
