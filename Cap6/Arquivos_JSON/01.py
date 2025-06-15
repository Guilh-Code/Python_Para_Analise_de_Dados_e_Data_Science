# Criando um dicionário
dict_guido = {'nome': 'Guido van Rossum',
'linguagem': 'Python',
'similar': ['c', 'Modula-3', 'lisp'],
'users': 1000000}

for k, v in dict_guido.items():
    print(k, v)

# importando o módulo JSON
import json

# Convertendo o dicionário para um objeto json
json.dumps(dict_guido)

# Criando um arquivo Json
with open('arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido))

# Leitura de arquivos Json
with open('arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)
print(dados['nome'])