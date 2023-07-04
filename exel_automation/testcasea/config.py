import requests

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'https://127.0.0.1:7890',
}

url = 'https://api.mexlucky.com/api/v1/vip-user/info'
data = {
    "token": "3f70f53d3cc44efaa294ad53aa0eda1f",
    "user_id": "63ea1db1a6e0d82545eac88b"
}

response = requests.post(url=url, json=data)
print(response.json())
