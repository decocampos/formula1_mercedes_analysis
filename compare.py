import pandas as pd
import matplotlib.pyplot as plt

class Piloto:
    def __init__(self, dados):
        self.dados = pd.DataFrame(dados)
        self.dados['date'] = pd.to_datetime(self.dados['date'])
        self.limitar_valores()

    def limitar_valores(self):
        self.dados['throttle'] = self.dados['throttle'].apply(self.limit_values)
        self.dados['brake'] = self.dados['brake'].apply(self.limit_values)

    @staticmethod
    def limit_values(value):
        return max(0, min(99, value))

    def plotar_dados(self, subplot_index, titulo):
        plt.subplot(2, 1, subplot_index)
        plt.plot(self.dados['date'], self.dados['throttle'], label='Throttle', color='green')
        plt.plot(self.dados['date'], self.dados['brake'], label='Brake', color='red')
        plt.title(titulo)
        plt.xlabel('Date')
        plt.ylabel('Values (0-99)')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

class ComparadorPilotos:
    def __init__(self, piloto_1, piloto_2):
        self.piloto_1 = piloto_1
        self.piloto_2 = piloto_2

    def exibir_graficos(self):
        plt.figure(figsize=(10, 12))
        self.piloto_1.plotar_dados(1, 'Throttle vs Brake Over Time - Piloto 1 (0-99)')
        self.piloto_2.plotar_dados(2, 'Throttle vs Brake Over Time - Piloto 2 (0-99)')
        plt.show()



