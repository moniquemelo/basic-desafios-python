class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos, pesa {self.peso}kg e possui {self.altura}m de altura.'

    def envelhecer(self):
        if self.idade < 21:
            self.crescer(0.005)
        self.idade += 1

    def engordar(self, ganho):
        self.peso += ganho

    def emagrecer(self, perda):
        self.peso -= perda

    def crescer(self, aumento):
        self.altura += aumento



p1 = Pessoa('Wesley', 20, 69.3, 1.76)
p2 = Pessoa('Monique', 25, 60.2, 1.69)

print(p1)
p1.envelhecer()
p1.engordar(5)
print(p1)
print()
print(p2)
p2.envelhecer()
p2.engordar(2)
print(p2)
p1.emagrecer(10)
print(p1)