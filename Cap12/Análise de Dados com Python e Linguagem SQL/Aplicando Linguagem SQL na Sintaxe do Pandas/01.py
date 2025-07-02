import sqlite3
import pandas as pd

# Conecta no banco de dados
con = sqlite3.connect('c:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap12/Análise de Dados com Python e Linguagem SQL/cap12_dsa.db')

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

print()

# A query abaixo retorna todas as linhas e todas as colunas da tabela.abs

# Cria uma instrução SQL
query = 'SELECT * FROM tb_vendas_dsa'

# Executa a query no banco de dados
cursor.execute(query)

# Retorna os dados da execução da query
dados = cursor.fetchall()
# print(dados)

# Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido',
                                    'ID_Cliente',
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])

print(df.head())
print()

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()

# A query abaixo retorna a média de unidades vendidas

# Calcula a média de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()

print(type(media_unidades_vendidas))
print(media_unidades_vendidas)
print()

# A query abaixo retorna a média de unidades vendidas por produto

# Calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produtos = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()

# Visualiza os 10 primeiros resultados
print(media_unidades_vendidas_por_produtos.head(10))
print()

# A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199
media_unidades_vendidas_por_produtos_se_for_maior_que_199 = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()

print(media_unidades_vendidas_por_produtos_se_for_maior_que_199)
print()

# A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199 e somente se a média de unidades vendidas for maior do que 10

# Alternativa A
Alternativa_A = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)

print(Alternativa_A)