class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostraCor(self):
        print(self.cor)

    def trocaCor(self, cor):
        self.cor = cor


bola1 = Bola('vermelho', 10, 'plastico')
bola1.mostraCor()
bola1.trocaCor('azul')
bola1.mostraCor()
