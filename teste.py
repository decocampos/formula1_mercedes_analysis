import requests
import time
from pydub import AudioSegment
import requests
from io import BytesIO
'''IMPORTAÇÕES'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

# URL da API
api_url = "https://api.openf1.org/v1/team_radio?session_key=9574&driver_number=63"

# Faz a requisição à API
response = requests.get(api_url)
response.raise_for_status()  # Levanta uma exceção se a requisição falhar

# Extrai os dados JSON da resposta
data = response.json()
# Função para buscar e reproduzir o áudio
def play_recording(url):
    chrome_driver_path = r'C:\Users\USER\Documents\formula1_mercedes_analysis\chromedriver.exe'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(chrome_driver_path, options=options)
    driver.get(f'{url}')
    time.sleep(15)
    driver.quit()

# Itera sobre cada dicionário na lista de dados e reproduz o áudio
for item in data:
    recording_url = item.get("recording_url")
    if recording_url:
        play_recording(recording_url)
    else:
        print("No recording_url found in item")
