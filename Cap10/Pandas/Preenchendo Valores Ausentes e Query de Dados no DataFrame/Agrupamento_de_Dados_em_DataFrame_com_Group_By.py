import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/Preenchendo Valores Ausentes e Query de Dados no DataFrame/dataset.csv")
print()

'''
    A função Pandas GroupBy é uma função versátil e fácil de usar que ajuda a obter uma visão
geral dos dados. Isso torna mais fácil explorar o conjunto de dados e revelar os relacionamentos
entre as variáveis.

    O código a seguir agrupará as linhas com base nas combinações Segmento/Valor_Venda e nos dará
a taxa média de vendas de cada grupo.
'''

# Aplicamos o group by
print(dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean())

'''
    Na instrução acima, primeiro filtramos os dados extraindo 3 colunas: [Segmento, Regiao,
Valor_Venda]. Na sequência, agrupamos por duas colunas: [Segmento, Regiao]. E então calculamos
a média para a coluna que ficou foram do group by, nesse caso Sales.

    O comportamento do group by com Pandas é o mesmo observado na Linguagem SQL.
'''