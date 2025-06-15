import pandas as pd

arquivo = "arquivos/salarios.csv"

df = pd.read_csv(arquivo) # usamos 'pd' no lugar de 'pandas'

print(df.head())


print(df['Position Title'].value_counts())