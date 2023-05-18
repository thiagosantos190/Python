class Bidu:
    def __init__(self,nome,raca,cor,peso,idade,porte) -> None:
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.idade = idade
        self.porte = porte

    def comer(self):
        print('Estou com fome')

    def latir(self):
        print('o Cachorro Latiu')

    def set_peso(self):
        return self.peso
    
    def set_idade(self):
        return self.idade
    
    def set_nome(self):
        return self.nome
    
    def set_cor(self):
        return self.cor
    


dog2 = Bidu('pingo','cofap','caramelo',6,4,'pequeno')
dog2.comer()
dog2.latir()

dog2.set_cor()
dog2.set_comer()
dog2.set_latir()
dog2.set_idade()
dog2.set_nome()

  
        
