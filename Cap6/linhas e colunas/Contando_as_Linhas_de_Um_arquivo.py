f = open('arquivos/salarios.csv', 'r')

data = f.read()

rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(',')
    full_data.append(split_row)

count = 0
for row in full_data:
    count += 1

print(count)