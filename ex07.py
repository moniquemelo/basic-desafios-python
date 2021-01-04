class Tamagushi:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def __str__(self):
        return f'{self.nome} está com {self.fome}% de fome, saude de {self.saude}% e {self.idade} ano(s) ' \
               f'e seu humor atual é {self.getHumor()}.'

    def setNome(self, nome):
        self.nome = nome

    def setFome(self, fome):
        self.fome = fome

    def setSaude(self, saude):
        self.saude = saude

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

    def getHumor(self):
        humor = self.saude - self.fome
        if humor <= 0:
            return f"\033[31mRIP {self.nome.upper()}\033[m, CEU DOS TAMAGUSHI :'("
        elif humor <= 40:
            return f'{self.nome} está PUTO!'
        elif humor <=70:
            return f'{self.nome} está suave'
        else:
            return f'{self.nome} está \033[32mTOO MUCH HAPPY :)\033[m'



t1 = Tamagushi('Batatinha', 10, 90, 1)
t2 = Tamagushi('Jumentinho', 100, 0, 10)
t2.setSaude(100)
t2.setFome(0)
print(t1)
print(t2)