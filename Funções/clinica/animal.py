class Animal:
    def __init__(self,name,color) -> None:
        self.name = name
        self.color = color

    def mover(self):
        print(f'{self.name} ANDOU')

    def pular(self):
        print(f'{self.name} PULOU')

a1 = Animal('bilu','caramelo')
a1.mover()

class Gato(Animal):
    pass

class Cachorro(Animal):
    pass
    def latir(self):
        print('AU AU AU')

class Coelho(Animal):
    pass

gato1 = Gato('josé','Branco')
gato1.mover()

cachoro1 = Cachorro('Matheus',"Preto")
cachoro1.mover()

Coelho1 = Coelho('lucas','Loiro')
cachoro1.pular()
cachoro1.latir()