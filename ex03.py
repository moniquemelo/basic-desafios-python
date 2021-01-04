class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def setLados(self, base, altura):
        self.base = base
        self.altura = altura

    def getLados(self):
        return self.base, self.altura

    def calcularArea(self):
        return self.base * self.altura

    def perimetroArea(self):
        return self.base * 2 + self.altura * 2


if __name__ == '__main__':
    base = int(input('Base: '))
    altura = int(input('Altura: '))

    b1 = Retangulo(base, altura)
    print(f'Você precisa de {b1.calcularArea()}m² de piso.')
    print(f'Você precisa de {b1.perimetroArea()}m de rodapé.')