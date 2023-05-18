from animal import Animal

class Peixe(Animal):
    def __init__(self,name,color,peso):
        super().__init__(name,color)
        self.peso = peso

    def mover(self):
        print(f'{self.name} NADOU')


a1 = Animal('Bilu','Caramelo')
a1.mover()

p1 = Peixe('Nemo','blue',5)
p1.mover()






