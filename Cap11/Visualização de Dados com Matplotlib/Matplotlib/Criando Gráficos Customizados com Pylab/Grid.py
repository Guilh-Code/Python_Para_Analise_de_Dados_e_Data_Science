# O PyLab combina funcionalidades do pyplot com funcionalidades do NumPy
from pylab import *

# Grid

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria os subplots
fig, axes = plt.subplots(1, 2, figsize = (10, 3))

# Grid padrão
axes[0].plot(x, x**2, x, x**3, lw = 2)
axes[0].grid(True)

# Grid customizado
axes[1].plot(x, x**2, x, x**3, lw = 2)
axes[1].grid(color = 'b', alpha = 0.7, linestyle = 'dashed', linewidth = 0.8)
show()