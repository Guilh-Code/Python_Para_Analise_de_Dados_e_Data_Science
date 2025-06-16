import re

texto = 'Meu e-mail é exemplo@gmail.com e você pode me contratar em outro_email@yahoo.com.'

# Expressão regular para contar quantas vezes o caractere arroba aparece no texto
resultado = len(re.findall('@', texto))
print(f"O caractere '@' apareceu {resultado} vezes no texto.")


# Expressão regular para extrair a palavra que aparece após a palavra 'você' em um texto
resultado = re.findall(r'você (\w+)', texto)
print(f"A palavra após 'você' é: {resultado[0]}")