# Extração de Arquivo da Web

from urllib.request import urlopen
import json

# API correta do Vimeo que retorna JSON
url = 'https://vimeo.com/api/v2/video/57733101.json'

# Lendo e decodificando a resposta
response = urlopen(url).read().decode('utf8')

# A resposta é uma lista com um único dicionário
dados = json.loads(response)[0]  # Pegamos o primeiro item

# Imprimindo os dados formatados
print(json.dumps(dados, indent=2))

# Exibindo informações específicas
print(f"Título: {dados['title']}")
print(f"URL: {dados['url']}")
print(f"Duração: {dados['duration']} segundos")
print(f"Número de Visualizações: {dados['stats_number_of_plays']}")
