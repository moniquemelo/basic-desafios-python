import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        
    def Iniciar(self):
        print('-='* 20)
        print('\033[35mVAMOS JOGAR? Chute um número entre 1 a 100 e tente acertar!\033[m')
        print('-= '* 20)
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
          
        try:
            while self.tentar_novamente == True:
                if int(self.chute) > self.valor_aleatorio:
                    print('\033[31mChute um valor mais BAIXO!\033[m')
                    self.PedirValorAleatorio()
                elif int(self.chute) < self.valor_aleatorio:
                    print('\033[34mChute um valor mais ALTO!\033[m')
                    self.PedirValorAleatorio()
                elif int(self.chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print(f'\033[32mNúmero: {self.valor_aleatorio}\nPARABÉNS! VOCÊ ACERTOU!\033[m')
        except:
            print('\033[31mResposta inválida. Digite um número inteiro entre 0 e 100!\033[m')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()