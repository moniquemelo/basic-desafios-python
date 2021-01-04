class Quadrado:

    def __init__(self, tamanho):
        self.tamanho = tamanho

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho):
        self.tamanho = tamanho

    def calcularArea(self):
        return self.tamanho ** 2


if __name__ == '__main__':
    q1 = Quadrado(5)
    print(q1.getTamanho())
    print(q1.calcularArea())
    q1.setTamanho(10)
    print(q1.getTamanho())
    print(q1.calcularArea())
