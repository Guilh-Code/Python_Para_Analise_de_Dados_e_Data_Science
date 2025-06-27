# O PyLab combina funcionalidades do pyplot com funcionalidades do NumPy
from pylab import *

# Dados
xx = np.linspace(-0.75, 1., 100)  # Gera 100 valores entre -0.75 e 1
n = np.array([0, 1, 2, 3, 4, 5])  # Números inteiros para os gráficos de barra e degrau

# Cria uma figura com 1 linha e 4 colunas de subplots, com tamanho 12x3
fig, axes = plt.subplots(1, 4, figsize=(12, 3))

# 1️⃣ Gráfico de dispersão (scatter)
axes[0].scatter(xx, xx + 0.25 * randn(len(xx)), color='black')
axes[0].set_title('scatter')

# 2️⃣ Gráfico de degrau (step)
axes[1].step(n, n ** 2, lw=2, color='blue')
axes[1].set_title('step')

# 3️⃣ Gráfico de barras (bar)
axes[2].bar(n, n ** 2, align='center', width=0.5, alpha=0.5, color='magenta')
axes[2].set_title('bar')

# 4️⃣ Área entre curvas (fill_between)
axes[3].fill_between(xx, xx ** 2, xx ** 3, alpha=0.5, color='green')
axes[3].set_title('fill_between')

# Exibe os gráficos
show()
