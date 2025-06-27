'''
Matplotlib é uma biblioteca de visualização de dados em Python amplamente utilizada para criar gráficos e visualizações de alta qualidade em diversas áreas, como ciência de dados, engenharia, finanças, estatística, entre outras. É uma biblioteca extremamente poderosa, flexível e personalizável, que permite a criação de gráficos em 2D e 3D, histogramas, diagramas de dispersão, gráficos de linhas, entre outros.

O Matplotlib oferece uma grande variedade de estilos de plotagem, tipos de gráficos e configurações de plotagem para personalização de gráficos. Ele é compatível com vários formatos de arquivos de imagem, como PNG, PDF, SVG, entre outros, permitindo a geração de imagens de alta qualidade para uso em publicações e apresentações.

Além disso, o Matplotlib é uma biblioteca de código aberto e gratuita, com uma comunidade ativa de desenvolvedores e usuários, o que significa que há uma grande quantidade de documentação, exemplos e suporte disponíveis online.
'''

import matplotlib as mpl


'''
                                CONSTRUINDO PLOTS

Plot é uma representação gráfica de dados em uma figura. Em outras palavras, é um gráfico que mostra a relação entre duas ou mais variáveis. Um plot pode ser criado usando uma biblioteca de visualização de dados, como o Matplotlib em Python.

Os tipos mais comuns de plots incluem gráficos de linhas, gráficos de dispersão, histogramas e gráficos de barras. Cada tipo de plot é adequado para diferentes tipos de dados e propósitos de visualização. Por exemplo, um gráfico de linhas é útil para visualizar tendências em uma série temporal, enquanto um gráfico de dispersão é útil para mostrar a relação entre duas variáveis contínuas.

A criação de um plot envolve a escolha dos dados a serem plotados, a seleção do tipo de plot e a configuração das opções de plotagem, como tamanho da figura, rótulos de eixo, título, cores, entre outros. Um plot bem criado pode fornecer insights valiosos sobre os dados, facilitando a compreensão e a comunicação das informações.
'''

# O matplotlib.pyplot é uma coleção de funções e estilos do Matplotlib
import matplotlib.pyplot as plt

# O método plot() define os eixos do gráfico
plt.plot([1, 3, 5], [2, 4, 7])
plt.show()

x = [2, 3, 5]
y = [3, 5, 7]

plt.plot(x, y)
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')
plt.title('Teste Plot')
plt.show()

x2 = [1, 2, 3]
y2 = [11, 12, 15]

plt.plot(x2, y2, label = 'Gráfico com Matplotlib')
plt.legend()
plt.show()
