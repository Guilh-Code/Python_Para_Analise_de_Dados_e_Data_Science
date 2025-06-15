f = open('arquivos/salarios.csv', 'r')

data = f.read()

rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)

print(full_data) 