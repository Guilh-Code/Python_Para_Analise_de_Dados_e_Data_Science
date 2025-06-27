'''
                                   Gráfico de Área Empilhada

Stack plots, também conhecidos como gráficos de área empilhada, são um tipo de plotagem usados para visualizar a mudança relativa de diversas variáveis ao longo do tempo. Eles consistem em várias áreas coloridas empilhadas umas sobre as outras, onde a altura de cada área representa a magnitude da variável correspondente e a largura representa a escala de tempo.

Os stack plots são úteis para mostrar como as partes contribuem para o todo ao longo do tempo. Por exemplo, eles podem ser usados para visualizar a mudança relativa de diferentes setores de uma indústria ao longo do tempo, ou a distribuição relativa de receitas e despesas de uma empresa em um determinado período.
'''

import matplotlib as mpl
import matplotlib.pyplot as plt

dias = [1, 2, 3, 4, 5]
dormir = [7, 8, 6, 77, 7]
comer = [2, 3, 4, 5, 3]
trabalhar = [7, 8, 7, 2, 2]
passear = [8, 5, 7, 8, 13]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m', 'c', 'r', 'k', 'b'])
plt.show()
