#Informations of the sessions

import requests
import json
url = "https://api.openf1.org/v1/sessions"

payload = ""
headers = ""
querystring = {"year":2024}
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
if response.status_code == 200:
    data = response.json()
    json_formatado = json.dumps(data, indent=4, ensure_ascii=False)
    print(json_formatado)
else:
    print("Erro ao fazer a requisição:", response.status_code)