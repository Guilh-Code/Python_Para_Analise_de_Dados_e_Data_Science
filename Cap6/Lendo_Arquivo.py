# Abrindo o arquivo para leitura
arql = open("arquivos/arquivo1.txt", "r") # r = read

# Lendo o arquivo
print(arql.read())

# Contar o número de caracteres
print(arql.tell())

# Retornar para o início do arquivo
print(arql.seek(0, 0))

# Lendo os primeiros 23 caracteres
print(arql.read(23))

# Lendo o arquivo
print(arql.read())