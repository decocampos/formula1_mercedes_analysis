import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime, timedelta
import numpy as np

# Função para buscar dados da API
def fetch_data(start_time, end_time):
    url = f"https://api.openf1.org/v1/location"
    payload = ""
    headers = ""
    querystring = {'session_key':9590,'driver_number':16,'date>':{start_time.isoformat()},'date<':{end_time.isoformat()}}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response)
    if response.status_code == 200:
        return response.json()

    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

# Inicializa uma lista para armazenar os dados
dados = {
    "x": [],
    "y": []
}

# Criação do DataFrame a partir dos dados iniciais
df = pd.DataFrame(dados)

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(12, 6))

# Variáveis globais para controle do tempo
start_time = datetime.fromisoformat('2024-09-01T13:15:00+00:00')
end_time = start_time + timedelta(milliseconds=600)
final_time = datetime.fromisoformat('2024-09-01T13:18:00+00:00')

# Inicializa o ponto anterior para a animação
previous_point = {"x": 0, "y": 0}

# Cria uma lista para armazenar os objetos de dispersão para os novos pontos
scatter_points = []

def update_plot(new_x, new_y):
    """Adiciona o novo ponto com animação suave, sem limpar o gráfico."""
    # Animação do novo ponto aparecendo
    t = np.linspace(0, 1, 10)  # 10 frames para animação suave
    for i in t:
        interpolated_x = previous_point['x'] * (1 - i) + new_x * i
        interpolated_y = previous_point['y'] * (1 - i) + new_y * i

        # Adiciona o ponto animado no gráfico
        point = ax.scatter(interpolated_x, interpolated_y, c='red', edgecolor='black')

        # Adiciona a pausa para criar o efeito de animação
        plt.pause(0.05)

        # Remove o ponto anterior para evitar sobreposição visual
        if scatter_points:
            scatter_points[-1].remove()

        # Guarda o ponto atual para futura remoção
        scatter_points.append(point)

    # Plota o novo ponto final (sem animação)
    final_point = ax.scatter(new_x, new_y, c='blue')
    scatter_points.append(final_point)

def animar(i):
    """Anima o gráfico com novos dados recebidos da API."""
    global start_time, end_time, df, previous_point

    if end_time <= final_time:
        print(f"Fetching data from {start_time.isoformat()} to {end_time.isoformat()}")
        data = fetch_data(start_time, end_time)
        if data:
            for entry in data:
                novo_ponto = {"x": entry["x"], "y": entry["y"]}
                df = pd.concat([df, pd.DataFrame([novo_ponto])], ignore_index=True)

                # Atualiza o gráfico com animação entre o ponto anterior e o novo ponto
                update_plot(novo_ponto['x'], novo_ponto['y'])

                # Atualiza o ponto anterior para o próximo ciclo de animação
                previous_point = novo_ponto

        # Avançar o intervalo de tempo
        start_time = end_time + timedelta(seconds=5)
        end_time = start_time + timedelta(seconds=5)

    return ax,

# Configura a animação para chamar a função animar a cada 1000 ms (1 segundo)
ani = animation.FuncAnimation(fig, animar, frames=range(1, 100), interval=1000, repeat=False)

# Remover a legenda e bordas desnecessárias
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Real-time Scatter Plot of x vs y')

plt.tight_layout()
plt.show()
