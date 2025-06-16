# Podemos trabalhar com módulos dos pacotes (quando disponível)

# Importando o módulo request do pacote urllib, usado para trazer url's Para dentro do nosso ambiente Python
import urllib.request

# Variável reposta armazena o objeto de conexão à url passada como parâmetro
resposta = urllib.request.urlopen('http://python.org')

# Objeto resposta
print(resposta)

# Chamando o método read() do objeto resposta e armazenando o código html na variável html
html = resposta.read()

print(html)