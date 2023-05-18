class Livro:
    def __init__(self,Nome,Autor,Editora,Paginas) -> None:

       self.Nome = Nome
       self.Autor = Autor
       self.Editora = Editora
       self.Paginas = Paginas

    def get_qt_paginas(self):
        print(self.Paginas)

    def get_editora(self):
        print(self.Editora)

    def set_alterarEditora(self,NovaEditora):
        self.Editora = NovaEditora

livro1 = Livro('História do Brasil','Desconhecido','Saraiva',500)
livro1.get_qt_paginas()
livro1.set_alterarEditora("Globo Livros")
livro1.get_editora()


