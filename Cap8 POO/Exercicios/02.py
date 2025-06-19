# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2 métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos especiais

class Pessoa():

    def __init__(self):
        self.nome = str(input('Digite seu nome completo: '))
        self.cidade = str(input('De que cidade você é: '))
        self.telefone = int(input('Digite seu número de telefone: '))
        self.email = input('Digite seu email: ')

    def __str__(self):
        return f'{self.nome} - {self.email}'

    def mostrar_cadastro(self):
        print(f"\nSeu nome é {self.nome}\nVocê mora na cidade de {self.cidade}")
        print(f"Seu telefone é {self.telefone}\nEmail: {self.email}")

# Criando objeto
pes = Pessoa()

# Chamando o método normal
pes.mostrar_cadastro()

# Chamando o método especial __str__
print(f"\nDados resumidos: {pes}")