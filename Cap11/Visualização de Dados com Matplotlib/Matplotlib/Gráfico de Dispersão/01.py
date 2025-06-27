'''
                                    Gráfico de Dispersão

Gráfico de dispersão, também conhecido como gráfico de pontos, é um tipo de plotagem utilizado para representar a relação entre duas variáveis contínuas. Cada ponto no gráfico de dispersão representa um par de valores das duas variáveis, onde uma variável é plotada no eixo horizontal e outra no eixo vertical.
'''

import matplotlib as mpl
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 5, 6, 8, 4, 8]

plt.scatter(x, y, label = 'Pontos', color = 'black', marker = 'o')
plt.legend()
plt.show()

