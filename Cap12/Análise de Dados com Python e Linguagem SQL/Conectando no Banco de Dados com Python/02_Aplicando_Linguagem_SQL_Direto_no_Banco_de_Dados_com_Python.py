import sqlite3
import pandas as pd

# Conecta no banco de dados
con = sqlite3.connect('c:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap12/Análise de Dados com Python e Linguagem SQL/cap12_dsa.db')

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

print()

# A Query abaixo retorna a média de unidades vendidas.

# Cria uma instrução SQL para calcular a média de unidades vendidas
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'

# Executa a query no banco de dados
cursor.execute(query2)

# Visualiza o resultado
print(cursor.fetchall())


# A query abaixo retorna a média de unidades vendidas por produto

# Cria uma instrução SQL para calcular a média de unidades vendidas por produto
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'

# Executa a query no bando de dados
cursor.execute(query3)

# Visualiza o resultado
print(cursor.fetchall())

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()