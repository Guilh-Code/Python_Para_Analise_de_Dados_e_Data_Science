# Criando a classe Livro com parâmetros no método construtor
class Livro():
    
    def __init__(self,titulo,isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto desta classe.")

    def imprime(self, titulo, isbn):
         print("Foi criado o livro %s com ISBN %d" %(titulo, isbn))

# Criando o objeto Livro2 que é uma instância da classe Livro
Livro2 = Livro("O Poder do Hábito", 77886611)

print(Livro2.titulo)

# Método do objeto Livro2
Livro2.imprime("O Poder do Hábito", 77886611)

print('-'*20)

# Criando a classe cachorro
class Algoritmo():

    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe.")

# Criando um objeto a partir da classe
algo1 = Algoritmo(tipo_algo = 'Random Forest')
algo2 = Algoritmo(tipo_algo = 'Deep Learning')

# Atributo da classe
print(algo1.tipo)
print(algo2.tipo)