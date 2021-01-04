class TV:

    def __init__(self, canal, volume, status=False):
        self.canal = canal
        self.volume = volume
        self.status = status

    def ligarDesligar(self):
        if self.status:
            self.status = False
        else:
            self.status = True

    def setCanal(self, canal):
        if not self.status:
            print('TV desligada, zé mané!')
        elif canal < 0 or canal > 25:
            print(f'Canal {canal} não existe!')
        else:
            self.canal = canal

    def setVolume(self, volume):
        if not self.status:
            print('TV desligada, MEU DEUS, PARA DE SER BURRO!')
        elif 0 <= volume <= 100:
            self.volume = volume
        else:
            print('Você não pode mais alterar o volume.')


sony = TV(17, 60)
sony.ligarDesligar()
sony.setVolume(20)
print(sony.volume)