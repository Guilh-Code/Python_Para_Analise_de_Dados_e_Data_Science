'''
                                        Histogramas

Histogramas são um tipo de plotagem utilizado para visualizar a distribuição de uma variável contínua. Eles são compostos por barras retangulares adjacentes, onde a área de cada barra é proporcional à frequência de observações de dados que caem em uma faixa específica de valores.

No histograma, a variável contínua é dividida em faixas de valores, conhecidas como intervalos de classe. O eixo horizontal representa os intervalos de classe, enquanto o eixo vertical representa a frequência de observações de dados que caem em cada intervalo de classe. Os intervalos de classe devem ser escolhidos de forma apropriada para a distribuição dos dados e a escala dos eixos deve ser definida adequadamente.

Os histogramas são úteis para visualizar a forma e a dispersão de uma distribuição de dados contínuos, como a altura de uma população ou as pontuações de um teste. Eles podem ajudar a identificar a presença de valores atípicos ou outliers nos dados e fornecer insights importantes sobre a distribuição dos dados.
'''

# O PyLab combina funcionalidades do pyplot com funcionalidades do NumPy
from pylab import *


# Dados
n = np.random.randn(100000)

# Cria os subplots
fig, axes = plt.subplots(1, 2, figsize = (12, 4))

# Plot 1
axes[0].hist(n)
axes[0].set_title('Histograma Padrão')
axes[0].set_xlim((min(n), max(n)))

# Plot 2
axes[1].hist(n, cumulative = True, bins = 50)
axes[1].set_title('Histograma Cumulativo')
axes[1].set_xlim((min(n), max(n)))

show()