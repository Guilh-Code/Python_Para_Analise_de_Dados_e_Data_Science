import sqlite3
import pandas as pd

# Conecta no banco de dados
con = sqlite3.connect('c:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap12/Análise de Dados com Python e Linguagem SQL/cap12_dsa.db')

# Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

print()

# A query retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199

# Cria uma instrução SQL para calcular a média de unidades por produto, quando o valor unitário for maior que 199
query4 = '''SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto'''

# Executa a query no banco de dados
cursor.execute(query4)

# Visualiza o resultado
print(cursor.fetchall())


# A query abaixo retorna a média de unidades vendidas por produto se o valor unitario for maior do que 199 e somente se a média de unidades vendidas for maior do que 10.

# Cria uma instrução SQL para calcular a média de unidades vendidas por produto, quando o valor unitario for maior que 199, mas somente se a média de unidades vendidas for maior que 10
query5 = '''SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10'''

# Executa a query no banco de dados
cursor.execute(query5)

# Visualiza o resultado
print(cursor.fetchall())

# Fecha o cursor e encerra a conexão
cursor.close()
con.close()