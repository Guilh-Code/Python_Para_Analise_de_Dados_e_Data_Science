# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():

    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

class MP3Player(Smartphone):

    def __init__(self, tamanho, interface, capacidade):
        super().__init__(tamanho, interface) # herda atributos de Smartphone
        self.capacidade = capacidade

    def mostrar_info(self):
        print(f"Tamanho do Smartphone: {self.tamanho}")
        print(f"Interface: {self.interface}")
        print(f"Capacidade do MP3: {self.capacidade} GB")


# Criando objeto da subclasse MP3Player
mp3 = MP3Player(6.5, "Toque e Voz", 128)

# Chamando método da classe MP3Player
mp3.mostrar_info()