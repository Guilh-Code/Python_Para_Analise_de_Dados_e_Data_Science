# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras
# Data e Science na frase: 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.

import re

texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

# Regex: encontra "Data Science" seguido de uma palavra
match = re.search(r'\bData\s+Science\s+(\w+)', texto)

if match:
    print("Palavra após 'Data Science':", match.group(1))
else:
    print("Padrão não encontrado.")
