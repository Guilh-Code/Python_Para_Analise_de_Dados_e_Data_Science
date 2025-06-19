# Mini-Desafio: Herança com Veículo e Carro

class Veiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        pass

class Carro(Veiculo):

    def __init__(self, marca, modelo, quantidade_portas):
        super().__init__(marca, modelo)
        self.quantidade_portas = quantidade_portas

    def __str__(self):
        return f"{self.marca} {self.modelo} com {self.quantidade_portas} portas"

    def exibir_info(self):
        print(f"Marca : {self.marca}")
        print(f"Modelo : {self.modelo}")
        print(f"Quantidade de Portas : {self.quantidade_portas}")

car = Carro('Toyota', 'Corolla', 4)
car.exibir_info()
print(f"\nDados resumidos: {car}")

print()

car2 = Carro('Honda', 'Civic', 4)
car2.exibir_info()
print(f"\nDados resumidos: {car2}")