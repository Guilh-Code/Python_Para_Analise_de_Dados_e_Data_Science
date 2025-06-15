# Abrindo arquivo para gravação
arq2 = open("arquivos/arquivo2.txt", "w") # w = write

# Como abrimos o arquivo apenas para gravação, não podemos usar comandos de leitura
# print(arq2.read())

# Gravando arquivo
arq2.write("Aprendendo a progranmar em Python.")

arq2.close()

# Lendo arquivo gravado
arq2 = open("arquivos/arquivo2.txt", "r")

print(arq2.read())

# Acrescentando conteúdo
arq2 = open("arquivos/arquivo2.txt", "a") # a = append

arq2.write(" E a metodologia de ensino da Data Science Academy facilita o aprendizado.")

arq2.close()

arq2 = open("arquivos/arquivo2.txt", "r")

print(arq2.read())

# Retornando ao início do arquivo para leitura
arq2.seek(0, 0)

print(arq2.read())