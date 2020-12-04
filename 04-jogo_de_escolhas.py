'''O objetivo desse jogo é sugerir algum campeão do League of Legends para o usuário jogar de acordo com suas preferencias.
Foi traçada uma pequena lista abaixo, sem muito critério e de maneira simplificada:

Campeões de Noxus Top: Darius(Tank), Sion(Tank), Kled(Lutador), Riven(Lutadora), Sion(Tank).
Campeões de Noxus Mid: Cassiopeia(Mago), Katarina (Assassina), Leblanc(Assassina), Swain(Mago), Vladimir(Mago).

Campeões de Demacia Top: Garen(tank), Kayle(Mago), Fiora(Lutadora) Poppy(Tank)
Campeões de Demacia Mid: Sylas(Mago), Lux(Mago), Morgana(Mago), Galio(Tank)
'''

class JogoDeEscolhas:
    def __init__(self):
        self.pergunta1 = 'Você quer seu campeão de Noxus ou Demacia? '
        self.pergunta2 = 'Prefere qual especialidade: Tank ou Mago? '
        self.pergunta3 = 'Prefere rota do Mid ou Top? '
        #Desfecho Noxus
        self.desfecho1 = '\033[32mNão foi encontrado o herói perfeito para você...\033[m'
        self.desfecho2 = '\033[32mVocê poderá jogar com Sion e Darius...\033[m'
        self.desfecho3 = '\033[32mVocê poderá jogar com Cassiopeia e Swain...\033[m'
        self.desfecho4 = '\033[32mVocê poderá jogar com Vladimir...\033[m'
        self.desfecho5 = '\033[32mVocê poderá jogar com Galio...'
        self.desfecho6 = '\033[32mVocê poderá jogar com Poppy e Garen...\033[m'
        self.desfecho7 = '\033[32mVocê poderá jogar com Morgana, Sylas e Lux...\033[m'
        self.desfecho8 = '\033[32mVocê poderá jogar com Kayle...\033[m'

        #Desfecho Demacia
    
    def Iniciar(self):
        print('-='* 20)
        print('\033[35mDICAS DE CAMPEÕES DO LEAGUE OF LEGENDS\033[m')
        print('-='* 20)
        
        res = input(self.pergunta1).lower()
        if res == 'noxus':
            res1B = input(self.pergunta2).lower()
            res2B = input(self.pergunta3).lower()
            if res1B =='tank' and res2B == 'mid':
                print(self.desfecho1)
            if res1B == 'tank' and res2B == 'top':
                print(self.desfecho2)
            if res1B == 'mago' and res2B == 'mid':
                print(self.desfecho3)
            if res1B == 'mago' and res2B == 'top':
                print(self.desfecho4)
        elif res == 'demacia':
            res1B = input(self.pergunta2).lower()
            res2B = input(self.pergunta3).lower()
            if res1B =='tank' and res2B == 'mid':
                print(self.desfecho5)
            if res1B == 'tank' and res2B == 'top':
                print(self.desfecho6)
            if res1B == 'mago' and res2B == 'mid':
                print(self.desfecho7)
            if res1B == 'mago' and res2B == 'top':
                print(self.desfecho8)
        else: 
            print('\033[31mResposta inválida. Tente novamente!\033[m')



jogo = JogoDeEscolhas()
jogo.Iniciar()