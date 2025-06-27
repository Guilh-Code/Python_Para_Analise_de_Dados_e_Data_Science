'''
                                        Gráfico de Pizza

Gráfico de Pizza (Pie Plot), também conhecido como gráfico de setores, é um tipo de plotagem que representa a composição de uma variável categórica em relação ao todo. Ele é representado por um círculo dividido em fatias que representam as proporções relativas das categorias.

Cada fatia do gráfico de pizza corresponde a uma categoria e sua área é proporcional à porcentagem que a categoria representa do todo. A categoria mais representativa é geralmente posicionada na parte superior do círculo, enquanto as outras fatias são posicionadas em sentido horário.

Os gráficos de pizza são comumente usados para mostrar a distribuição de dados em relação ao todo e para destacar as proporções relativas de diferentes categorias. Por exemplo, um gráfico de pizza pode ser usado para mostrar a distribuição de vendas por produto em uma empresa ou a distribuição de votos por partido em uma eleição.
'''

import matplotlib as mpl
import matplotlib.pyplot as plt

fatias = [7, 2, 2, 13]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']

plt.pie(fatias, labels = atividades, colors = cores, startangle = 90, shadow = True, explode = (0, 0.2, 0, 0))
plt.show()