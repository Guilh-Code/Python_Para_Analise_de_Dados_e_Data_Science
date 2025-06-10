print('Bem-Vindo à Calculadora\n')

while True:
    try:
        n1 = float(input('Digite o Primeiro número: '))
        break
    except ValueError:
        print('ERRO! Digite um número')

while True:
    try:    
        n2 = float(input('Digite o Segundo número: '))
        break
    except ValueError:
        print('ERRO! Digite um número')

operador = input('Selecione o operador (+, -, *, /): ')

if operador == '+':
    soma = n1 + n2
    print(f'O resultado foi {soma}')
elif operador == '-':
    sub = n1 - n2
    print(f'O resultado foi {sub}')
elif operador == '*':
    mult = n1 * n2
    print(f'O resultado foi {mult}')
elif operador == '/':
    if n1 == 0 or n2 == 0:
        print('Não pode dividir um número por 0. Tente novamente')
    else:
        div = n1 / n2
        print(f'O resultado foi {div}')
else:
    print('Operador Inválido')