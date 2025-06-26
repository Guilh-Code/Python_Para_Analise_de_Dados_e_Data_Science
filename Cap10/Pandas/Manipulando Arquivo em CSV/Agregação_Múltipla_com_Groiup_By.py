import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/Manipulando Arquivo em CSV/dataset.csv")
print()

'''
    Vamos explorar mais a função groupby() pois temos diversas opções de sumarização dos dados
de forma simples. No exemplo abaixo uniremos a função groupby() com a função agg() para realiza agregação múltipla.
'''

# Aplicamos o group by
print(dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count']))

'''
    Na instrução acima, primeiro filtramos os dados extraindo 3 colunas: [Segmento, Regiao,
Valor_Venda]. Na sequência, agrupamos por duas colunas: [Segmento, Regiao]. E então agregamos
os dados calculando a média, desvio padrão e contagem de elementos para a coluna que ficou fora
do group by, nesse caso a coluna Valor_Venda

    A função agg() recebe como argumento uma lista de funções para agregação
'''