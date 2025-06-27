# O PyLab combina funcionalidades do pyplot com funcionalidades do NumPy
from pylab import *


# Gráficos de linha em Paralelo

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Divide a área de plotagem em dois subplots
fig, axes = plt.subplots(nrows = 1, ncols = 2)

# Loop pelos eixos para criar cada plot
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Título')

# Ajusta o layout
fig.tight_layout()
show()