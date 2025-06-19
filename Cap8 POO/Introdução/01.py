# Class em Python é um molde (modelo) que define como criar objetos com características (atributos) e comportamentos (métodos).

# Criando uma Classe chamada Livro
class Livro():

    # Esse método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__
    # (self) é uma referência a cada atributo da própria classe(e não de uma classe mãe, por exemplo)
    def __init__(self):

        # Atributos são propriedades
        self.titulo = 'Sapiens - Uma Breve História da Humanidade'
        self.isbn = 998888
        print("Construtor chamado para criar um objeto desta classe.")

    # Métodos são funções que executam ações nos objetos da classe
    def imprime(self):
        print("Foi criado o livro %s com ISBN %d" %(self.titulo, self.isbn))


# Criando uma instância da classe Livro
Livro1 = Livro()

# O objeto Livro1 é do tipo Livro
print(type(Livro1))

# Atributo do objeto Livro1
print(Livro1.titulo)

# Método do objeto
print(Livro1.imprime())