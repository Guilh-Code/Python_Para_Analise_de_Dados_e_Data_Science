# Foi solicitado à você uma classe Funcionário, cujos atributos são: nome e e-mail. Deve-se guardar as horas trabalhadas em um dicionário, cujas chaves são o mês em questão e, em outro dicionário, guardar o salário por hora relativo ao mês em questão.

'''
Além disso, precisamos de um método que retorna o salário mensal do funcionário. A proposta é que sejam separados em dois arquivos:

um chamado funcionario.py, em que será criada a classe com suas funcionalidades.

um segundo chamado teste_funcionario.py, em que você deve aplicar testes e verificar a legitimidade do código anterior.
'''

class Funcionario:
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    def cadastro_hora(self, mes, horas):
        if (mes not in self.horas):
            self.horas[mes] = horas

    def cadastro_salario_hora(self, mes, valor):
        if (mes not in self.salario_hora):
            self.salario_hora[mes] = valor

    def calcula_salario(self, mes):
        if (mes not in self.horas) or (mes not in self.salario_hora):
            print("Mês Inexistente!!")
        else:
            return self.horas[mes] * self.salario_hora[mes]

    def __repr__(self):
        return f"\nFuncionário: {self.nome}, \nEmail: {self.email}, \nHoras/Mês: {self.horas}, \nSalário-Hora: {self.salario_hora}"