import requests
import json
#
# url = "https://aajogo-api.pre-release.xyz/game/double_speed/bet"
#
# payload = json.dumps({
#    "bet_amount": 10,
#    "currency": "brl",
#    "color": "Red"
# })
# headers = {
#    'authorization': '6369c5bf04ad3c83508722bf;96c4ab50514e4608b231d0fc438cad4c',
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.json())

url = 'https://aajogo-api.pre-release.xyz'
double = '/game/double_speed/bet'

x = url+double
data = {
   "bet_amount": 10,
   "currency": "brl",
   "color": "Red"
}
headers = {
   'authorization': '6369c5bf04ad3c83508722bf;96c4ab50514e4608b231d0fc438cad4c',
}

request = requests.post(url=x, json=data, headers=headers)

print(request.json())

if not headers:
    print("Headers are empty.")
else:
    print("Headers are not empty.")