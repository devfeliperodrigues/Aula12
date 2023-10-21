"""Faça uma classe chamada livro com os atributos:
        título do livro
        autor do livro
        gênero do livro
        Número de páginas
e as Funções:

    exibir informações completas do livro (título, autor, gênero, Páginas)

    verificar se o livro é longo (considerar livros longos que contenha mais do que 350 páginas)"""



from classes import *

livro1 = Livro("Brumas de Avalon", "Marion Eleanor Zimmer Bradley", "Fantasia", 968 )

livro2 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Ficção", 208 )

livro3 = Livro("Sociedade do Cansaço", "Byung-chul Han", "Filosofia",136 )



livro3.Exibir()
livro3.Verificar()