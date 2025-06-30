import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import warnings
warnings.filterwarnings("ignore")

# Construindo um dataframe com Pandas
df = pd.DataFrame()
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(55, 100), 30)

print(df.shape)
print(df.head())

# lmplot (cria automaticamente em figura separada)
sea.lmplot(data=df, x='idade', y='peso', fit_reg=True)

# Kdeplot idade
plt.figure()
sea.kdeplot(df.idade)
plt.title("Distribuição KDE - Idade")

# Kdeplot peso
plt.figure()
sea.kdeplot(df.peso)
plt.title("Distribuição KDE - Peso")

# distplot (ainda funciona, mas está depreciado — usamos displot ou histplot hoje em dia)
plt.figure()
sea.distplot(df.peso)
plt.title("Distplot - Peso")

# Histograma + rugplot
plt.figure()
plt.hist(df.idade, alpha=0.3)
sea.rugplot(df.idade)
plt.title("Histograma com Rugplot - Idade")

# Boxplot idade
plt.figure()
sea.boxplot(df.idade, color='m')
plt.title("Boxplot - Idade")

# Boxplot peso
plt.figure()
sea.boxplot(df.peso, color='y')
plt.title("Boxplot - Peso")

# Violinplot idade
plt.figure()
sea.violinplot(df.idade, color='g')
plt.title("Violinplot - Idade")

# Clustermap
plt.figure()
sea.clustermap(df)

# Exibe todos os gráficos
plt.show()
