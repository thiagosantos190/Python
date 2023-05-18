class Filme:
    def __init__(self,nome,duracao) -> None:
        self.nome = nome
        self.duracao = duracao

    def get_ExibirPlay(self):
        print('filme iniciou')
    
film = Filme('rei leão',130)
film.get_ExibirPlay()

        