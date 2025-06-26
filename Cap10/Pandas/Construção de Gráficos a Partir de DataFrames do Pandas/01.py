# Vimos até aqui diversas funcionalidades do Pandas que tornam o processo de manipulação de dados realmente simples. E para concluir este capítulo vamos estudas as opções que o Pandas oferece para criação de gráficos diretamente a partir de dataframes, sem a necessidade de usar qualquer outra biblioteca.


# Importa o Scikit-learn (usado para acessar o dataset Iris)
import sklearn

# Importa especificamente a função para carregar o dataset Iris
from sklearn.datasets import load_iris

# Carrega o dataset Iris (um dos datasets mais famosos para treino em ML e visualização)
data = load_iris()

# Importa a biblioteca Pandas para manipulação de dados em formato de tabelas (DataFrames)
import pandas as pd

# Cria um DataFrame a partir dos dados do Iris
# data['data'] contém os dados das flores (medidas numéricas)
# data['feature_names'] contém os nomes das colunas (características das flores)
df = pd.DataFrame(data['data'], columns=data['feature_names'])

# Adiciona uma nova coluna chamada 'species' com os rótulos das espécies (0, 1, 2)
# Usamos from_codes para converter os números nas categorias com nome
df['species'] = pd.Categorical.from_codes(data['target'], data['target_names'])

# Mostra as 5 primeiras linhas do DataFrame no terminal
print(df.head())
print('-=' * 32)  # Separador visual no terminal

# -------------------------------------------
# INÍCIO DOS GRÁFICOS
# -------------------------------------------

# Importa a biblioteca Matplotlib (necessária para exibir os gráficos)
import matplotlib.pyplot as plt

# 1️⃣ Gráfico de linhas com todas as variáveis numéricas
# Por padrão, será um gráfico de linha com cada linha representando uma amostra
df.plot()
plt.title("Gráfico de Linhas - Todas as Variáveis")
plt.show()  # Exibe o gráfico
print('-=' * 32)

# 2️⃣ Scatter plot (dispersão) entre comprimento e largura da sépala
# Útil para ver a relação entre duas variáveis
df.plot.scatter(x='sepal length (cm)', y='sepal width (cm)', title="Scatter - Sépalas")
plt.show()
print('-=' * 32)

# 3️⃣ Gráfico de área para algumas colunas
# Gráfico de área destaca a acumulação dos valores
columns = ['sepal length (cm)', 'petal length (cm)', 'petal width (cm)', 'sepal width (cm)']
df[columns].plot.area(title="Gráfico de Área - Algumas Variáveis")
plt.show()

# 4️⃣ Gráfico de barras agrupado por espécie
# Aqui tiramos a média de cada característica para cada espécie
# Isso ajuda a comparar as espécies com base nas médias de cada variável
df.groupby('species').mean().plot.bar(title="Média das Variáveis por Espécie")
plt.show()

# 5️⃣ Gráfico de pizza com a contagem de amostras por espécie
# Útil para visualizar a distribuição das classes
df['species'].value_counts().plot.pie(
    title="Distribuição de Espécies",
    autopct='%1.1f%%'  # Mostra porcentagem com 1 casa decimal
)
plt.ylabel("")  # Remove o rótulo do eixo Y para melhorar o visual
plt.show()

# 6️⃣ Gráficos de densidade KDE para todas as variáveis
# KDE (Kernel Density Estimation) mostra uma curva suavizada da distribuição dos dados
df.plot.kde(
    subplots=True,     # Cria um gráfico separado para cada variável
    figsize=(8, 8),     # Define o tamanho da figura
    title="Distribuição KDE das Variáveis"
)
plt.tight_layout()      # Ajusta o layout para não sobrepor os textos
plt.show()

# 7️⃣ Boxplot de cada variável numérica
# Esse tipo de gráfico ajuda a visualizar a mediana, quartis e possíveis outliers
df[columns].plot.box(figsize=(8, 8), title="Boxplot das Variáveis")
plt.tight_layout()
plt.show()