# *** Aula 05 ***

# Geração de Dados
import numpy as np
import matplotlib.pyplot as plt

tam_populacao = 10000
np.random.seed(2000)

# Gráfico
lst_dados = []
for i in range(2):
	dados = np.random.normal(loc=100, scale=10, size=tam_populacao)

	plt.hist(dados);
	plt.xlabel("Categorias");
	plt.ylabel("Quantidade");
	plt.hist(x=dados, bins="auto", color="#0805aa", alpha=0.7, rwidth=0.85, density=True)
	plt.grid(axis="y", alpha=0.80)
	
	plt.xlabel("Categorias");
	plt.ylabel("Quantidade");
	plt.title("Histograma das Amostras");
	lst_dados.append(dados)

# Teste de Hipóteses
from scipy.stats import ttest_ind

dados1 = lst_dados[0]
dados2 = lst_dados[1]

estatistica, p_valor = ttest_ind(dados1, dados2)

print("estatistica=%.3f, p_valor=%.3f" % (estatistica, p_valor))

if p_valor > 0.05:
	print("Aceita H0")
else:
	print("Rejeita H0")
