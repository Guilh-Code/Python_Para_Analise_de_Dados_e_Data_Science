# Métodos de classe são funções definidas dentro de uma classe, que permitem que os objetos criados a partir dessa classe executem ações.

# Criando uma classe chamada Circulo
class Circulo:

    # O valor de pi é constante
    pi = 3.14

    # Quando um objeto desta classe for criado, este método será executado e o valor do raio será 5
    def __init__(self, raio = 5):
        self.raio = raio

    # Esse método calcula a área
    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    # Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    # Método para obter o raio do círculo
    def getRaio(self):
        return self.raio

# Criando o objeto circ, uma instância da classe Circulo
circ = Circulo()

# Executando um método da classe Circulo
print(circ.getRaio())

# Criando outro objeto chamado circ1. Uma instância da classe Circuito()
# Agora sobrescrevendo o valor do atributo
circ1 = Circulo(7)

# Executando um método da classe Circulo
print(circ1.getRaio())

# Imprimindo o raio
print(f"O raio é: {circ.getRaio()}")

# Imprimindo a área
print(f"Área igual a: {circ.area()}")

# Gerando um novo valor para o raio do círculo
circ.setRaio(3)

# Imprimindo o novo raio
print(f"Novo raio igual a: {circ.getRaio()}")