"""Nome, saúde, energia

métodos: 
brincar
comer
lutar
descansar

brincar faz ele gastar 10 de energia
lutar faz ele gastar 20 de energia
comer faz ele recuperar 10 de energia
descansar faz ele recuperar 20 de energia"""

class Tomagotchi():
    def __init__(self, nome:str, saude:int, energia:int, experiencia:float, inteligencia:float, nivel:int, felicidade:float, moedas:int):
        self.nome = nome
        self.saude = 100
        self.energia = 100
        self.experiencia = 10
        self.inteligencia = 5
        self.nivel = 0
        self.felicidade = 100
        self.moedas = 0


    def brincar(self):
        self.saude - 10
        self.felicidade +20

    def comer(self):
        escolha_user = int(input(print("""Que tipo de comida você quer dar para seu Tomagotchi?
        1 - Fruta
        2 - Sorvete
        3 - Arroz
        4 - Pizza
        5 - Hamburguer""")))

        if escolha_user == 1:
            self.saude + 10
            self.felicidade -1
            self.energia +5

        elif escolha_user == 2:
            self.felicidade + 15
            self.energia +10

        elif escolha_user == 3:
            self.felicidade + 5
            self.energia + 15
            self.saude + 5

        elif escolha_user == 4:
            self.felicidade + 20
            self.energia + 15

        else:
            self.felicidade + 25
            self.energia + 20

    def lutar(self):
        self.saude - 20
        self.experiencia * 1.15
        self.felicidade - 5
        self.moedas + 10

    def descansar(self):
        self.saude + 20
        self.felicidade +5

    def ler(self):
        self.saude -2
        self.experiencia + (self.inteligencia * .1 )
        self.inteligencia + 10
    
    def evolucao(self):
        if self.experiencia >= 20:
            self.nivel +1
            self.felicidade + 20
            self.saude + 50
            print(f"{self.nome} evoluiu de nível!!! Agora ele é nível {self.nivel}")
    
def Novo_tomagotchi():
    novo_tomagotchi = Tomagotchi(nome = input("Digite o Nome do seu Tomagotchi: " ))
    return

def Menu():
    escolha_usuario = input("""Escolha uma opção:
    1 - Alimentar 
    1 - Checar Saúde 
    1 - Alimentar Tomagotchi 
    1 - Alimentar Tomagotchi 
    1 - Alimentar Tomagotchi """)