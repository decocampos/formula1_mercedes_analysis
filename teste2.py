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
    
    def definir_tempos(self, minuto1, segundo1, milisegundo1, minuto2, segundo2, milisegundo2):
        self.tempo_piloto_1 = f'{minuto1}:{segundo1:02}:{milisegundo1:03}'
        self.tempo_piloto_2 = f'{minuto2}:{segundo2:02}:{milisegundo2:03}'

    def exibir_graficos(self):
        plt.figure(figsize=(15, 10))

        # Ajustar o layout para adicionar distância entre os gráficos
        plt.subplots_adjust(hspace=4, top=85)

        # Gráfico para o throttle
        plt.subplot(2, 1, 1)
        plt.plot(self.piloto_1.dados.index, self.piloto_1.dados['throttle'], label='Throttle Piloto 1', color='blue')
        plt.plot(self.piloto_2.dados.index, self.piloto_2.dados['throttle'], label='Throttle Piloto 2', color='yellow')
        plt.title('Throttle Comparison')
        plt.xlabel('Index')
        plt.ylabel('Throttle (0-99)')
        plt.legend()
        plt.xticks(rotation=45)

        # Gráfico para o brake
        plt.subplot(2, 1, 2)
        plt.plot(self.piloto_1.dados.index, self.piloto_1.dados['brake'], label='Brake Piloto 1', color='blue')
        plt.plot(self.piloto_2.dados.index, self.piloto_2.dados['brake'], label='Brake Piloto 2', color='yellow')
        plt.title('Brake Comparison')
        plt.xlabel('Index')
        plt.ylabel('Brake (0-99)')
        plt.legend()
        plt.xticks(rotation=45)

        # Adicionando gráfico de comparação de tempo na mesma figura
        plt.gcf().text(0.75, 0.95, f'Piloto 1: {self.tempo_piloto_1}\nPiloto 2: {self.tempo_piloto_2}', 
                        ha='left', va='top', fontsize=12, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.5'))

        plt.tight_layout()
        plt.show()

        


