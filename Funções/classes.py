class Cachorro:
    def __init__(self,nome,raca,cor,peso, idade, porte) -> None:
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.porte = porte
        self.idade = idade

    def comer(self):
        print('Estou com fome AU AU')
                        

    def latir(self):
        print('AU AU')

    def mostraNome(self):
        print(self.nome)

    def dormir(self):
        print('Estou dormindo')
    
    
dog1 = Cachorro('pingo','cofap','caramelo',6,4,'pequeno')
dog1.latir()
dog1.mostraNome()
dog1.dormir()





