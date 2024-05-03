# Exemplo Prático de Amostragem

import numpy as np
import matplotlib.pyplot as plt

# Geração de dados da população
tamanho_populacao = 10000
np.random.seed(2006)
dados_populacao = np.random.normal(loc=100, scale=10, size=tamanho_populacao)

plt.hist(dados_populacao)
plt.xlabel("Altura da Árvore")
plt.ylabel("Quantidade de Árvores")

# Amostragem
tamanho_amostra = 50
qtd_simulacoes = 10
medias_amostra = []

for x in range (qtd_simulacoes):
    media_amostra = np.random.choice(dados_populacao, size=tamanho_amostra).mean()
    medias_amostra.append(media_amostra)

medias_amostra = np.array(medias_amostra)

# Gráfico
plt.hist(x=medias_amostra, bins='auto', color='#0705ba', alpha=0.7, rwidth=0.85, density=True)
plt.grid(axis='y', alpha=0.80)
plt.xlabel("Médias das alturas das amostras")
plt.ylabel("Frequência de ocorrência")
plt.title("Histograma das Médias das Amostras")

plt.show()
