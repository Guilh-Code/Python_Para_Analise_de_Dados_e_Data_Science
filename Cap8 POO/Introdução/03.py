# Em Python, tudo é OBJETO!

# Criando uma lista
lst_num = ["Data", "Science", "Acadamy", "Nota", 10, 10]

# A lista lst_num é um objeto, uma instância da classe lista em Python
print(type(lst_num))

print(lst_num.count(10))

# Usamos a função type, para verificar o tipo de um objeto
print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type('a'))

# Criando um novo tipo de objeto chamado Carro
class Carro(object):
    pass

# Instância do Carro
ferrari = Carro()

print(type(ferrari))

# Criando uma classe
class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

# Criando um objeto chamado Estudante1 a partir da classe Estudantes
Estudantes1 = Estudantes("Bob", 12, 9.5)

# Atributo da classe Estudante, utilizado por cada objeto criado a partir desta classe
print(Estudantes1.nome)
print(Estudantes1.idade)
print(Estudantes1.nota)

# Criando uma classe
class Funcionarios:

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def listFunc(self):
        print(f"Funcionário {self.nome} tem salário de R${self.salario} e o cargo é {self.cargo}")

# Criando um objeto chamado Func1 a partir da classe Funcionarios
Func1 = Funcionarios("Mary", 20000, "Cientista de Dados")

# Usando o método da classe
Func1.listFunc()

print('-'*30)

print("***** Usando Atributos *****")

print(hasattr(Func1, "nome"))
print(hasattr(Func1, "salario"))
print(setattr(Func1, "salario", 4500))
print(hasattr(Func1, "salario"))
print(getattr(Func1, "salario"))
print(delattr(Func1, "salario"))
print(hasattr(Func1, "salario"))