# A função filter() é usada para filtrar elementos de um iterável, retornando apenas aqueles que satisfazem uma condição (ou seja, para os quais a função retorna True).

# Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Chamando a função e passando um parâmetro. retornará Falso se for ímpar e True se for par.
print(verificaPar(35))
print(verificaPar(10))

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

# A função filter() retorna um iterator
print(filter(verificaPar, lista))
print(list(filter(verificaPar, lista)))

print('-'*25)

print(list(filter(lambda x: x%2==0, lista)))
print(list(filter(lambda num: num > 8, lista)))
x