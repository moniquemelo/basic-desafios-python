class Macaco:

    def __init__(self, nome, bucho=None):
        if bucho is None:
            bucho = []
        self.nome = nome
        self.bucho = bucho

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        if self.bucho:
            print(f'O {self.nome} tá com a pança cheia de: {self.bucho}')
        else:
            print(f'{self.nome}, seu bucho está só VERME.')

    def digerir(self):
        self.bucho.clear()

m1 = Macaco('Chico')
m2 = Macaco('Devfracassado', ['Pizza', 'Avestruz'])

m2.digerir()
m2.verBucho()
m2.comer('Bacalhau')
m2.comer('Miojo')
m2.comer('Pipoca')
m2.verBucho()
m1.verBucho()
m1.comer('Camarão')
m1.verBucho()
m2.digerir()
m2.verBucho()