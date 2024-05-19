# Aula 04

import scipy.stats as st
import math

# Estimação de Parâmetros
nv_confianca = 0.95
nv_significancia = 1 - nv_confianca

Z = abs(st.norm.ppf(nv_significancia/2))
#print(f'Z = {Z}')

# Intervalo de Confiança
tm_populacao = 60
desv_padrao = 0.020
desv_padrao_amostral = desv_padrao/math.sqrt(tm_populacao)

md_amostral = 0.01

lim_sup = md_amostral + Z*desv_padrao_amostral
lim_inf = md_amostral - Z*desv_padrao_amostral
intv_confianca = (md_amostral - lim_inf, md_amostral + lim_sup)

print(f'Intervalo de Confiança = {intv_confianca}')