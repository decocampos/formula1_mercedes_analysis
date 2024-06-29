'''from urllib.request import urlopen
import json

response = urlopen('https://api.openf1.org/v1/car_data?driver_number=44')
data = json.loads(response.read().decode('utf-8'))
print(data)'''
import requests
#Gran Prix information
url = "https://api.openf1.org/v1/meetings"

payload = ""
headers = ""
querystring = {"year":2024,"country_name":"Spain"}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Erro ao fazer a requisição:", response.status_code)

#Section of te race: FP1, FP2, FP3, Quali, Race, Sprint
url2 = "https://api.openf1.org/v1/sessions"

payload = ""
headers = ""
querystring = {"year":2024,"country_name":"Spain"}
response = requests.request("GET", url2, data=payload, headers=headers, params=querystring)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Erro ao fazer a requisição:", response.status_code)