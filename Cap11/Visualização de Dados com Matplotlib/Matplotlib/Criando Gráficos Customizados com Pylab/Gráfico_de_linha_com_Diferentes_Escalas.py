# O PyLab combina funcionalidades do pyplot com funcionalidades do NumPy
from pylab import *

# Gráfico de linha com diferentes escalas

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria os subplots
fig, axes = plt.subplots(1, 2, figsize = (10, 4))

# Cria o plot1
axes[0].plot(x, x**2, x, exp(x))
axes[0].set_title('Escala Padrão')

# Cria o plot2
axes[1].plot(x, x**2, x, exp(x))
axes[1].set_yscale('log')
axes[1].set_title('Escala Logaritmica (y)')
show()