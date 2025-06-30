import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import warnings
warnings.filterwarnings("ignore")


# Carrega o dataset "tips" que já vem com o Seaborn
dados = sea.load_dataset("tips")

# Mostra as 5 primeiras linhas do DataFrame
print(dados.head())

# O método jointplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot(data = dados, x = 'total_bill', y = 'tip', kind = 'reg')

# O método lmplot() cria plot com dados e modelos de regressão
sea.lmplot(data = dados, x = 'total_bill', y = 'tip', col = 'smoker')

# 🔽 Exibe todos os gráficos criados acima
plt.show()
