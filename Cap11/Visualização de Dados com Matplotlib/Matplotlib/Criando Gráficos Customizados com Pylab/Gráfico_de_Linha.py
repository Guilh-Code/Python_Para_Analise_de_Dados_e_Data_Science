'''
                                Criando Gráficos Customizados com Pylab

Pylab é um módulo fornecido pela biblioteca Matplotlib que combina a funcionalidade do pacote NumPy com a funcionalidade do pacote pyplot. Ele fornece um ambiente de plotagem interativo, permitindo que os usuários criem rapidamente gráficos e visualizações de dados.

O módulo Pylab inclui muitas funções úteis para plotagem de gráficos, como funções para criar gráficos de linha, gráficos de dispersão, gráficos de barras, gráficos de pizza, histogramas e muito mais. Ele também fornece funções para personalizar as configurações de plotagem, como títulos de eixo, rótulos de eixo, títulos de gráfico e cores.
'''

# O PyLab combina funcionalidades do pyplot com funcionalidades do NumPy
from pylab import *

'''
                                        Gráfico de Linha

Gráfico de linha é um tipo de plotagem usado para representar a evolução do comportamento de uma variável com diferentes pontos de dados. O gráfico normalmente é usado com variáveis contínuas.

No gráfico de linha, cada ponto de dados é representado por um ponto na linha. A linha conecta os pontos de dados.

Os gráficos de linha são úteis para visualizar tendências e padrões em dados contínuos ao longo do tempo. Por exemplo, eles podem ser usados para mostrar a variação da temperatura ao longo de um período de tempo, a evolução da população em uma região ou a flutuação do valor de uma ação na bolsa de valores.
'''

# Gráfico de linha

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria a figura
fig = figure()

# Define posição e tamanho dos eixos: [esquerda, baixo, largura, altura]
axes = fig.add_axes([0, 0, 0.8, 0.8])

# Plota os dados
axes.plot(x, y, 'r')  # 'r' = linha vermelha

# Define os rótulos dos eixos e o título
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha')

# Mostra o gráfico
show()