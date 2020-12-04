'''Sugestão incrementos ao projeto:
1 - Colocar uma inteface gráfica simples.
2 - Colocar o simulador dentro de um looping com pergunta de 'Deseja continuar?'''


import random 
class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de jogar o dado? '        

    def Iniciar(self):
        res = input(self.mensagem).lower().strip()
        
        try:
            if res == 'sim' or res =='s':
                print('Número:', end=' ')
                self.ValorDoDado()                                   
            elif res == 'não' or res == 'n':
                print('Agradecemos sua participação. Volte novamente em breve!')
            else:
                print('Resposta inválida. Favor digitar Sim ou Não!')
        except:
            print('Ocorreu um erro ao receber sua resposta')


    def ValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))      

  
simulador = SimuladorDeDado()
simulador.Iniciar()




