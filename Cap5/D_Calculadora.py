def Menu_Calc():
    print('********** Calculadora em Python **********')
    print('\n1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

def Soma(a, b):
    return print(f'{a} + {b} = {a+b}')
    
def Subtracao(a, b):
    return print(f'{a} - {b} = {a-b}')

def Multiplicacao(a, b):
    return print(f'{a} * {b} = {a*b}')

def Divisao(a, b):
    return print(f'{a} / {b} = {a/b}')

Menu_Calc()
opcao = int(input('\nDigite sua opção (1/2/3/4): '))

n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print()

if opcao == 1:
    Soma(n1, n2)
elif opcao == 2:
    Subtracao(n1, n2)
elif opcao == 3:
    Multiplicacao(n1, n2)
elif opcao == 4:
    Divisao(n1, n2)
else:
    print('Opção Inválida!')