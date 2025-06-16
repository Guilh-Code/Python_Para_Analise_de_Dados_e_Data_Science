texto = 'Meu e-mail é exemplo@gmail.com e você pode me contratar em outro_email@yahoo.com.'

import re

# Expressão regular para extrair endereçoes de e-mail de uma string
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', texto)

print(emails)


print('-'*35)

text = 'O aluno estava incrivelmente perdido,mas encontrou a DSA e rapidamente começou a aprender.'

# Extraindo os advérbios da frase
for m in re.finditer(r"\w+mente\b", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
