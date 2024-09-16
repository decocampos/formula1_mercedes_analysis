from datetime import datetime, timedelta
from compare import Piloto, ComparadorPilotos
from teste2 import Piloto_teste, ComparadorPilotos_teste
import requests

# Definição da variável global
SESSION_KEY = 9586

def calc_time_btw_laps(date_start, lap_duration):
    date = datetime.fromisoformat(date_start)
    date_end = date + timedelta(seconds=lap_duration)
    return date_end

def info_lap(driver_number, lap):
    url = "https://api.openf1.org/v1/laps"
    payload = ""
    headers = ""
    querystring = {"session_key": SESSION_KEY, 'driver_number': driver_number, "lap_number": lap}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        lap_start = data[0]["date_start"]
        lap_finish = calc_time_btw_laps(data[0]["date_start"], data[0]["lap_duration"])
        return [lap_start, lap_finish]
    else:
        print("Erro ao fazer a requisição (laps):", response.status_code)

def car_data(driver_number, time):
    print(time)
    url = "https://api.openf1.org/v1/car_data"
    payload = ""
    headers = ""
    querystring = {"session_key": SESSION_KEY, 'driver_number': driver_number, 'date>': time[0], 'date<': time[1]}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao fazer a requisição (car_data):", response.status_code)

'''# Criação dos objetos piloto
lap_info_1 = info_lap(16, 3)
car_data_1 = car_data(16, lap_info_1)
piloto_1 = Piloto(car_data_1)

lap_info_2 = info_lap(55, 3)
car_data_2 = car_data(55, lap_info_2)
piloto_2 = Piloto(car_data_2)

# Comparação e exibição dos gráficos
comparador = ComparadorPilotos(piloto_1, piloto_2)
comparador.exibir_graficos()'''

# Criação dos objetos piloto
lap_info_1 = info_lap(4, 11)
car_data_1 = car_data(16, lap_info_1)
piloto_1 = Piloto_teste(car_data_1)

lap_info_2 = info_lap(81, 15)
car_data_2 = car_data(55, lap_info_2)
piloto_2 = Piloto_teste(car_data_2)

# Comparação e exibição dos gráficos
comparador = ComparadorPilotos_teste(piloto_1, piloto_2)
comparador.exibir_graficos()