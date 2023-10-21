class Cachorro():
    def __init__(self, nome:str, raca:str, peso:float):
        self.nome_cao = nome
        self.raca_cao = raca
        self.peso_cao = peso
    
    def raca(self):
        return f"""O {self.nome_cao} é da raça {self.raca_cao}, pesa {self.peso_cao}Kg e come **...croc croc croc...**"""
    
class Gato():
    def __init__(self, nome:str, raca:str, peso:float):
        self.nome_gato = nome
        self.raca_gato = raca
        self.peso_gato = peso
    
    def derubar_coisas(self):
        return f"""*** PLOFT***  O gato {self.nome_gato} quebrou algo... Ele tem {self.peso_gato}kg e sua raça é {self.raca_gato}"""