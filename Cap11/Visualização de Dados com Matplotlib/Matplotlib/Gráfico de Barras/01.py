'''
                                    Gráfico de Barras

Gráfico de barras é um tipo de plotagem usado para representar dados categóricos com barras retangulares. Cada barra representa uma categoria e a altura da barra representa a quantidade ou frequência da categoria.

O eixo horizontal do gráfico de barras mostra as categorias e o eixo vertical mostra a escala de medida dos dados. As barras podem ser vertical ou horizontal, dependendo da preferência do usuário.

Os gráficos de barras são comumente usados para comparar a quantidade ou frequência de diferentes categorias. Eles são úteis para mostrar diferenças entre grupos e ajudam a visualizar rapidamente quais categorias têm valores maiores ou menores.
'''

import matplotlib as mpl
import matplotlib.pyplot as plt

x1 = [2, 4, 6, 8, 10]
y1 = [6, 7, 8, 2, 4]

plt.bar(x1, y1, label = 'Barras', color = 'green')
plt.legend()
plt.show()

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

plt.bar(x1, y1, label = 'Listas1', color = 'blue')
plt.bar(x2, y2, label = 'Listas2', color = 'red')
plt.legend()
plt.show()

