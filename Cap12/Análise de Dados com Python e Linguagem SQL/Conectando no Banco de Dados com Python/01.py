import sqlite3
import pandas as pd

# Conecta no banco de dados
con = sqlite3.connect('c:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap12/Análise de Dados com Python e Linguagem SQL/cap12_dsa.db')

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

# Query SQL para extrair os nomes das colunas no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

# Executa a query
cursor.execute(sql_query)

# Visualiza o resultado
print()
print(cursor.fetchall())



# A query abaixo retorna todas as linhas e colunas da tabela.abs

# Cria uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'

# Executa a query no banco de dados
cursor.execute(query1)

# List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]

# Visualiza o resultado
print(nomes_colunas)

# Retorna os dados da execução da query
dados = cursor.fetchall()

# Visualiza os dados
print(dados)