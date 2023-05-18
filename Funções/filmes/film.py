from filme import*

class Acao(Filme):
    def __init__(self,nome,duracao,explodir) -> None:
        self.nome = nome
        self.duracao = duracao
        self.explodir = explodir

    def get_explodir(self):
        print('Explodiu')

gener = Acao("Operação Perigo",150,'explosão')
gener.get_explodir()

class Drama(Filme):
    pass
    def get_tragedia(self):
        print('que Tragédia e essa')

class Suspense(Filme):
    pass
    def get_expectativa(self):
        print('Expectativa')

genero1 = Suspense("a favorita",100)

genero1.get_expectativa()


filme1 = Drama("dramatico",180)
filme1.get_tragedia()




