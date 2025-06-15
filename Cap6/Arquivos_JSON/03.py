import json

# Nomes dos arquivos
arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/dados.txt'

# Método 1
with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)

# Método 2
open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())

# Leitura do arquivo txt
with open('arquivos/dados.txt', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)