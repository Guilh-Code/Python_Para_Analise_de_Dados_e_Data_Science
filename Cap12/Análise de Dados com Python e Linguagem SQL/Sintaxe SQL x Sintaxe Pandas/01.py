# As duas instruções abaixo retornam o mesmo resultado!

# Sintaxe SQL
query = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
           FROM tb_vendas_dsa
           WHERE Valor_Unitario > 199
           GROUP BY Nome_Produto
           HAVING AVG(Unidades_Vendidas) > 10"""

# Sintaxe Pandas
df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                              .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                              .groupby('Nome_Produto')['Unidades_Vendidas'].mean()