texto = 'Cientista de Dados pode ser uma excelente alternativa de carreira. \n'
texto = texto + 'Esses profissionais precisam saber como programar em Python. \n'
texto += 'E, claro, devem ser proficientes em Data Science.'


# Usando a Expressão WITH
# O método close() é executado automaticamente

with open('arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(len(conteudo))
print(conteudo)

with open('arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])

# Lendo o arquivo
arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)