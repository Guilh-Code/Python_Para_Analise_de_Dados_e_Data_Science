f = open('arquivos/salarios.csv', 'r')

data = f.read()

rows = data.split('\n')

print(rows)