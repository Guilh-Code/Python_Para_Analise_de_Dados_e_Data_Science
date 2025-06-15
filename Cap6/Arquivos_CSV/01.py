# Importanto o módulo csv
import csv

with open('arquivos/numeros.csv', 'w') as arquivo:

    # Cria um objeto de gravação
    writer = csv.writer(arquivo)

    # Grava no arquivo linha a linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63,87,92))
    writer.writerow((61,79,76))
    writer.writerow((72,64,91))

# Leitura do arquivo csv
with open('arquivos/numeros.csv', 'r', encoding='utf8', newline='\r\n') as arquivo:

    # Cria o objeto de leitura
    leitor = csv.reader(arquivo)
    # Loop
    for x in leitor:
        print(x)

# Gerando uma lista com dados do arquivo csv
with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)

# Imprimindo a partir da segunda linha
for linha in dados[1:]:
    print(linha)
    