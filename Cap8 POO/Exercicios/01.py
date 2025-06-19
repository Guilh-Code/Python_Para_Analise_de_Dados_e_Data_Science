# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada aos atributos e métodos

class Rocket(): 
        
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
            
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)

# Criando o objeto com x=5 e y=3
roc1 = Rocket(5, 3)

# Acessando atributos
print("x =", roc1.x)
print("y =", roc1.y)

# Usando os métodos
roc1.print_rocket()
roc1.move_rocket(2, 4)
roc1.print_rocket()