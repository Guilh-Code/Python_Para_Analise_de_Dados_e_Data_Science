import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/Manipulando Arquivo em CSV/dataset.csv")
print()

# Cuidado para não confundir. Vimos o Split e agora veremos o Strip. São funções diferentes.

# O Split divite strings. O Strip remove caracteres da string. Veja os exemplos.

print(dsa_df.head(3))
print('-='*23)

print(dsa_df['Data_Pedido'].head(3))

# A coluna 'Data_Pedido' é a data de envio do produto no formato YYYY-MM-DD. Imagine que seja necessário deixar o ano apenas com 2 dígitos sem alterar o tipo variável. Fazemos isso com a função lstrip(), ou seja, left strip.

# Vamos remover os dígitos 2 e 0 à esquerda do valor da variável 'Data_Pedido'
print(dsa_df['Data_Pedido'].str.lstrip('20'))

# Como não usamos o inplace = True a mudança é somente na memória e não altera o dataframe. Podemos usar ainda as funções rstrip() e strip() com diferentes variações de strip de strings.