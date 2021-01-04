class ContaCorrente:

    def __init__(self, conta, nome, saldo=0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def setNome(self, nome):
        self.nome = nome

    def depositar(self, dep):
        self.saldo += dep

    def sacar(self, saque):
        if saque > self.saldo:
            print('Você não tem saldo suficiente para sacar este valor.')
        else:
            self.saldo -= saque



c1 = ContaCorrente(101, 'Wesley')
c2 = ContaCorrente(202, 'Monique', 10000)
c1.setNome('Wesley Dias')
print(c1.nome)

c1.depositar(275)
print(c1.saldo)
print()
c2.sacar(10500)
print(c2.saldo)