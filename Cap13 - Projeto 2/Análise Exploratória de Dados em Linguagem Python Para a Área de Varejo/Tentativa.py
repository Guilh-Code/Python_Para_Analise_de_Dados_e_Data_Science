# Imports
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# CARREGANDO OS DADOS

# Carrega o dataset
df_dsa = pd.read_csv('c:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap13 - Projeto 2/dataset.csv')

# Shape
print()
print(df_dsa.shape)
print('-='*32)


# Amostra dos dados
print('Os 5 primeiros dados')
print()
print(df_dsa.head())
print('-='*32)

# Amostra dos dados
print('Os 5 últimos dados')
print()
print(df_dsa.tail())
print('-='*32)

# ANÁLISE EXPLORATÓRIA

# Colunas do conjunto de dados
print('COLUNAS DO CONJUNTO DE DADOS')
print()
print(df_dsa.columns)
print('-='*32)

# Verificando o tipo de cada coluna
print('VERIFICANDO O TIPO DE CADA COLUNA')
print()
print(df_dsa.dtypes)
print('-='*32)

# Resumo estatístico da coluna com o valor de venda
print('RESUMO ESTATÍSTICO DA COLUNA COM O VALOR DE VENDA')
print()
print(df_dsa['Valor_Venda'].describe())
print('-='*32)

# Verificando se há registros duplicados
print('VERIFICANDO SE HÁ REGISTROS DUPLICADOS')
print()
print(df_dsa[df_dsa.duplicated()])
print('-='*32)

# Verificando se há valores ausentes
print('VERIFICANDO SE HÁ VALORES AUSENTES')
print()
print(df_dsa.isnull().sum())
print('-='*32)

print('Dados')
print()
print(df_dsa.head())
print('-='*32)

print('='*30)
print('AVALIAÇÃO')
print('='*30)



# Pergunta de Negócio 1:
# Qual Cidade com maior Valor de Venda de produtos da categoria 'Office Supplies'?

# 1. Filtra os dados apenas da categoria "Office Supplies"
df_filtrado = df_dsa[df_dsa['Categoria'] == 'Office Supplies']

# 2. Agrupa por cidade e soma os valores de venda
vendas_por_cidade = df_filtrado.groupby('Cidade')['Valor_Venda'].sum()

# 3. Encontra a cidade com o maior valor de venda
cidade_maior_venda = vendas_por_cidade.idxmax()
valor_maior_venda = vendas_por_cidade.max()

print(f"A cidade com maior valor de venda em 'Office Supplies' é {cidade_maior_venda} com R${valor_maior_venda:.2f}")
print('-='*32)




# Pergunta de Negócio 2:
# Qual o total de Vendas por Data do Pedido?
# Demonstra o resultado através de um gráfico de barras.

# 1. Agrupa por data e soma as vendas
vendas_por_data = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()

# 2. Plota o gráfico de barras
plt.figure(figsize=(12,6))
plt.bar(vendas_por_data.index, vendas_por_data.values, color='skyblue')
plt.xlabel('Data do Pedido')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Data do Pedido')
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor leitura
plt.tight_layout()




# Pergunta de Negócio 3:
# Qual o total de vendas por estado?
# Demonstra o resultado através de um gráfico de barras.

# 1. Agrupa por estado e soma as vendas
total_vendas_por_estado = df_dsa.groupby('Estado')['Valor_Venda'].sum()

# 2. Plota o gráfico de barras
plt.figure(figsize=(12,6))
plt.bar(total_vendas_por_estado.index, total_vendas_por_estado.values, color = 'r')
plt.xlabel('Estados')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Estado')
plt.xticks(rotation=70)  # <- Isso melhora a leitura dos estados
plt.tight_layout()       # <- Garante que nada fique cortado

# Opção 2
df_dsa_p3 = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()

# Plot
plt.figure(figsize=(14,6))
sns.barplot(data = df_dsa_p3,
            y = 'Valor_Venda',
            x = 'Estado').set(title = 'Vendas Por Estado')
plt.xticks(rotation = 70)



# Pergunta do Negócio 4:
# Quais são as 10 cidades com Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de barras

total_vendas_por_cidades = df_dsa.groupby('Cidade')['Valor_Venda'].sum()


top_10_cidades = total_vendas_por_cidades.sort_values(ascending=False).head(10)

# 2. Plota o gráfico de barras
plt.figure(figsize=(12,6))
plt.bar(top_10_cidades.index, top_10_cidades.values, color = 'b')
plt.xlabel('Cidades')
plt.ylabel('Total de Vendas')
plt.title('Top 10 Cidades com MAIOR total de vendas!')
plt.xticks(rotation=65)
plt.tight_layout()

'''# OPÇÂO EM UMA LINHA DE CODIGO
df_dsa_p4 = df_dsa.groupy('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False).head(10)

# Plot 2
plt.figure(figsize=(16,6))
sns.set_palette('coolwars')
sns.barplot(data = df_dsa_p4,
            x = 'Valor_Venda',
            y = 'Cidade').set(title = 'As 10 Cidades com maior Total de Vendas')'''



# Pergunta do Negócio 5:
# Qual o segmento teve o maior total de Vendas?
# Demonstre o resultado através de um gráfico de pizza

# 1. Agrupa o segmento com o maior total de vendas
segmento_maior_vendas = df_dsa.groupby('Segmento')['Valor_Venda'].sum()

# 2. Plota o gráfico de pizza
plt.figure(figsize=(8,8))
plt.pie(segmento_maior_vendas, 
        labels = segmento_maior_vendas.index,
        autopct = '%1.1f%%',
        startangle = 90,
        shadow = True)
plt.title('Distribuição do Total de Vendas por Segmento')
plt.axis('equal') # Garante que o gráfico fique circular
plt.tight_layout()


# Pergunta de Negócio 6:
# Qual o total de vendas por Segmento e por Ano?

# 1. Garante que a data esteja em formato datetime
df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst=True)

# 2. Cria uma nova coluna com o ano da data
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year

# 3. Agrupa por Segmento e Ano e soma as vendas
total_segmento_ano = df_dsa.groupby(['Segmento', 'Ano'])['Valor_Venda'].sum()

print(total_segmento_ano)



# Pergunta de Negócio 7:
# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:

# - Se o Valor_Venda for maior que 1000 recebe 15% de desconto
# - Se o Valor_Venda for menor que 1000 recebe 10% de desconto

# Quantas Vendas Receberiam 15% de desconto?

vendas_com_15 = df_dsa[df_dsa['Valor_Venda'] > 1000]

quantidade = len(vendas_com_15)

print(f"O Número de vendas com 15% de desconto: {quantidade}")

# -----------------------------------

'''Exemplo do curso:

# Cria uma nova coluna de acordo com a regra definida acima
df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)

df_dsa.head()

# Total por cada valor da variável
df_dsa['Desconto'].value_counts()

print('No total 457 Vendas receberiam descontos de 15%')
'''

# -----------------------------------

# Pergunta de Negócio 8 (DESAFIO Nível Master):
# Considere que a empresa decida conceder o desconto de 15% do item anterior.
# Qual seria a média do valor venda antes e depois do desconto


# 1. Calcula a média sem desconto
media_sem_desconto = df_dsa['Valor_Venda'].mean()

# 2. Aplica desconto de 15% em TODAS as vendas
df_dsa['Valor_Venda_Com_Desconto'] = df_dsa['Valor_Venda'].apply(lambda x: x - (x * 0.15))

# 3. Calcula a média com desconto

media_com_desconto = df_dsa['Valor_Venda_Com_Desconto'].mean()

# 4. Mostra o resultado
print(f"Média do Valor de Venda SEM desconto: R$ {media_sem_desconto:.2f}")
print(f"Média do Valor de Venda COM desconto de 15%: R$ {media_com_desconto:.2f}")



# Pergunta de Negócio 9 (DESAFIO Nível Master Ninja):
# Qual o Média de Vendas por Segmento, por Ano e por Mês?
# Demonstre o resultado através de gráfico de linha.

'''# Cria colunas de Ano e Mês a partir da data
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year
df_dsa['Mes'] = df_dsa['Data_Pedido'].dt.month

# Agrupa por Segmento, Ano e Mês e calcula a MÉDIA de vendas
media_vendas = df_dsa.groupby(['Segmento', 'Ano', 'Mes'])['Valor_Venda'].mean().reset_index()
print(media_vendas[['Ano', 'Mes']].drop_duplicates().sort_values(['Ano', 'Mes']))

# Garante que a coluna Mes esteja formatada com dois dígitos (ex: 01, 09)
media_vendas['Mes'] = media_vendas['Mes'].apply(lambda x: f"{int(x):02d}")

# Cria a coluna de data no formato correto e explícito
media_vendas['Data'] = pd.to_datetime(
    media_vendas['Ano'].astype(str) + '-' + media_vendas['Mes'] + '-01',
    format='%Y-%m-%d'
)


# Cria uma coluna "Data" combinando Ano e Mês para plotagem
media_vendas['Data'] = pd.to_datetime(media_vendas['Ano'].astype(str) + media_vendas['Mes'].astype(str) + '-01')


# Agora plota um gráfico de linha para cada segmento
plt.figure(figsize=(12,6))

for segmento in media_vendas['Segmento'].unique():
    dados_segmento = media_vendas[media_vendas['Segmento'] == segmento]
    plt.plot(dados_segmento['Data'], dados_segmento['Valor_Venda'], marker = 'o', label = segmento)

plt.xlabel('Data')
plt.ylabel('Média de Vendas')
plt.title('Média de Vendas por Segmento, Ano e Mês')
plt.legend(title='Segmento')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()'''



# Pergunta de Negócio (DESAFIO Nível Master Ninja das Galáxias):
# Qual o total de vendas por Categoria e SubCategoria, considerando somente as top 12 SubCategorias?
# Demonstre tudo através de um único gráfico.


'''
JEITO QUE EU FIZ

# 1. Top 12 SubCategorias com maior valor de venda
top_12_subcategorias = df_dsa.groupby('SubCategoria')['Valor_Venda'].sum() \
                             .sort_values(ascending=False).head(12)

# 2. Filtra o DataFrame com base nas SubCategorias top 12
df_filtrado = df_dsa[df_dsa['SubCategoria'].isin(top_12_subcategorias.index)]

# 3. Agrupa por Categoria e SubCategoria e soma o valor de vendas
total_vendas = df_filtrado.groupby(['Categoria', 'SubCategoria'])['Valor_Venda'].sum()

# 4. Prepara os rótulos do eixo X combinando Categoria + SubCategoria
labels = [f'{cat} - {sub}' for cat, sub in total_vendas.index]

# 5. Plota o gráfico de barras
plt.figure(figsize=(14,6))
plt.bar(labels, total_vendas.values, color='teal')
plt.xlabel('Categoria - SubCategoria')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Categoria e SubCategoria (Top 12 SubCategorias)')
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
plt.show()'''

# Agrupamos por categoria e subcategoria e calculamos a soma somente para variávels numéricas
df_dsa_p10 = df_dsa.groupby(['Categoria',
'SubCategoria']).sum(numeric_only = True).sort_values('Valor_Venda', ascending= False).head(12)

# Convertemos a coluna Valor_Venda em número inteiro e classificamos por categoria
df_dsa_p10 = df_dsa_p10[['Valor_Venda']].astype(int).sort_values(by = 'Categoria').reset_index()

print(df_dsa_p10)

# Criamos outro dataframe somente com os totais por categoria
df_dsa_p10_cat = df_dsa_p10.groupby('Categoria').sum(numeric_only = True).reset_index()

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}%\n(${val:,})'
    return my_format


# Listas de cores para categorias
cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']

# Lista de cores para subcategorias
cores_subcategorias = ['#aa8cd4',
                        '#aa8cd5',
                        '#aa8cd6',
                        '#aa8cd7',
                        '#26c957',
                        '#26c958',
                        '#26c959',
                        '#26c960',
                        '#e65e65',
                        '#e65e66',
                        '#e65e67',
                        '#e65e68']


# Plot

# Tamanho da figura
fig, ax = plt.subplots(figsize = (18,12))

# Gráfico das categorias
p1 = ax.pie(df_dsa_p10_cat['Valor_Venda'],
            radius = 1,
            labels = df_dsa_p10_cat['Categoria'],
            wedgeprops = dict(edgecolor = 'white'),
            colors = cores_categorias)

# Gráfico das subcategorias
p2 = ax.pie(df_dsa_p10['Valor_Venda'],
            radius = 0.9,
            labels = df_dsa_p10['SubCategoria'],
            autopct = autopct_format(df_dsa_p10['Valor_Venda']),
            colors = cores_subcategorias,
            labeldistance = 0.7,
            wedgeprops = dict(edgecolor = 'white'),
            pctdistance = 0.53,
            rotatelabels = True)

# Limpa o centro do circulo
centre_circle = plt.Circle((0, 0), 0.6, fc = 'white')

# Labels e anotações
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.annotate(text = 'Total de Vendas : ' + '$ ' + str(int(sum(df_dsa_p10['Valor_Venda']))), xy = (-0.2, 0))
plt.title('Total de Vendas por Categoria e Top 12 SubCategoria')
plt.show()