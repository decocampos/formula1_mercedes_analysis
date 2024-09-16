import pandas as pd
import matplotlib.pyplot as plt

class Piloto_teste:
    def __init__(self, dados):
        self.dados = pd.DataFrame(dados)
        self.dados['date'] = pd.to_datetime(self.dados['date'])
        self.dados['index'] = self.dados.index
        self.limitar_valores()

    def limitar_valores(self):
        self.dados['throttle'] = self.dados['throttle'].apply(self.limit_values)
        self.dados['brake'] = self.dados['brake'].apply(self.limit_values)

    @staticmethod
    def limit_values(value):
        return max(0, min(99, value))

class ComparadorPilotos_teste:
    def __init__(self, piloto_1, piloto_2):
        self.piloto_1 = piloto_1
        self.piloto_2 = piloto_2

    def exibir_graficos(self):
        plt.figure(figsize=(12, 10))

        # Gráfico para o throttle
        plt.subplot(2, 1, 1)
        plt.plot(self.piloto_1.dados['index'], self.piloto_1.dados['throttle'], label='Throttle Piloto 1', color='blue')
        plt.plot(self.piloto_2.dados['index'], self.piloto_2.dados['throttle'], label='Throttle Piloto 2', color='yellow')
        plt.title('Throttle Comparison')
        plt.xlabel('Date')
        plt.ylabel('Throttle (0-99)')
        plt.legend()
        plt.xticks(rotation=45)

        # Gráfico para o brake
        plt.subplot(2, 1, 2)
        plt.plot(self.piloto_1.dados['index'], self.piloto_1.dados['brake'], label='Brake Piloto 1', color='blue')
        plt.plot(self.piloto_2.dados['index'], self.piloto_2.dados['brake'], label='Brake Piloto 2', color='yellow')
        plt.title('Brake Comparison')
        plt.xlabel('Date')
        plt.ylabel('Brake (0-99)')
        plt.legend()
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

