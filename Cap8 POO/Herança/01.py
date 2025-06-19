# Herança é um conceito da Programação Orientada a Objetos (POO) que permite criar uma nova classe a partir de outra classe existente. A nova classe (chamada classe filha ou subclasse) herda os atributos e métodos da classe original (chamada classe pai ou superclasse).

# Criando a classe Animal - Super-classe
class Animal:

    def __init__(self):
        print("Animal criado.")

    def imprimir(self):
        print("Este é um animal.")

    def comer(self):
        print("Hora de comer.")

    def emitir_som(self):
        pass

# Criando a classe Cachorro - Sub-Classe
class Cachorro(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Objeto Cachorro Criado.")

    def emitir_som(self):
        print("Au Au!")

# Criando a classe Gato - Sub-Classe
class Gato(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Objeto Gato criado.")

    def emitir_som(self):
        print("Miau!")

# Criando um objeto (Instanciando a classe)
rex = Cachorro()
zeze = Gato()

rex.emitir_som()
zeze.emitir_som()

# Executando o método da classe Cachorro (sub-classe)
rex.imprimir()

# Executando o método da classe Animal (super-classe)
rex.comer()

# Executando o método da classe Gato (sub-classe)
zeze.comer()