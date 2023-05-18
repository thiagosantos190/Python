class Automovel:
    def __init__(self,placa='hvt-3030') -> None:
        self.cor = placa
        self.placa = placa

    def dirigir(self,velocidade):
        print(f'Estou dirigindo a {velocidade} kmh')

    def get_placa(self):
        print(self.placa)

car1 = Automovel('HSX-2829')
car1.get_placa()
car1.dirigir(60)

car2 = Automovel('HSX-2829')
car2.get_placa()
car2.dirigir(70)
