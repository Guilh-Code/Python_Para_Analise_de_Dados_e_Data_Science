'''"# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local'''


total = 0
def soma( arg1, arg2 ):
    total = arg1 + arg2; 
    print(f'Dentro da função o total é: {total}')
    return total


soma(10, 20)
print(f'Fora da função o total é: {total}')