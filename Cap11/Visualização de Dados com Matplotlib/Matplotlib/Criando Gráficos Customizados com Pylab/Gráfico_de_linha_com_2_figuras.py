# O PyLab combina funcionalidades do pyplot com funcionalidades do NumPy
from pylab import *

# Gráficos de linha com 2 figuras

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria a figura
fig = plt.figure()

# Cria os eixos
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # eixos da figura principal
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # eixos da figura secundária

# Figura principal
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

# Figura secundária
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária')
show()