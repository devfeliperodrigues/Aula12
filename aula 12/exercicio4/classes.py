class Conta():
    def __init__(self, identificador,nome,saldo):
        self.identificador = identificador
        self.nome = nome
        self.saldo = saldo
    
    def Verificar(self):
        print(f"""Informações sobre a conta {self.identificador}:
                        Nome do Proprietário da conta: {self.nome}
                        Saldo existente da conta: {self.saldo}
                        
                        Obrigado pela preferência. Volte Sempre!""")
        

    def Deposito(self):
        deposito = float(input("Digite a quantia que você gostaria de depositar: "))
        self.saldo =+ deposito
        print(f"parabéns, você acabou de depositar R${deposito}")
        print(f"O seu alto atual é de {self.saldo}")
        
class Conta_corrente(Conta):
    def __init__(self, identificador, nome, saldo):
        super().__init__(identificador, nome, saldo)
        self.identificador = identificador
        self.nome = nome
        self.saldo = saldo
    
    def Sacar(self):
        sacar = float(input("Digite a quantia que deseja sacar: "))
        self.saldo =- sacar
        print(f"Você sacou {sacar}, o saldo atual é de {self.saldo}")

class Conta_poupanca(Conta):
    def __init__(self, identificador, nome, saldo):
        super().__init__(identificador, nome, saldo)
        self.identificador = identificador
        self.nome = nome
        self.saldo = saldo
    
    def juros(self):
        taxa_juros = (0.05/100)
        self.saldo = self.saldo * taxa_juros
        print(f"A taxa de juros é de {taxa_juros}. Com os juros aplicados, seu saldo atual de {self.saldo}")
