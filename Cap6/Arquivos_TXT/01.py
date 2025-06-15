texto = 'Cientista de Dados pode ser uma excelente alternativa de carreira. \n'
texto = texto + 'Esses profissionais precisam saber como programar em Python. \n'
texto += 'E, claro, devem ser proficientes em Data Science.'

print(texto)

# Importanto o módulo OS
import os

# Criando um arquivo
arquivo = open(os.path.join('arquivos/cientista.txt'), 'w')

# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + '')

# Fechando o arquivo
arquivo.close()