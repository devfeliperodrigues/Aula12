class Livro():
    def __init__(self, titulo:str, autor:str, genero:str, paginas:int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.paginas = paginas

    def Exibir(self):
        print(f"O título se chama '{self.titulo}', cujo autor se chama {self.autor}. O gênero é {self.genero} e o livro possui {self.paginas}.")

    def Verificar(self):
        if self.paginas > 350:
            print(f"Este livro possui {self.paginas}, considerado longo.")
        elif self.paginas < 20:
            print(f"Este livro possui apenas {self.paginas}, considerado um livreto.")
        else:
            print(f"Este livro possui {self.paginas}, considerado comum.")