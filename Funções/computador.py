class Computador:
    def __init__(self,marca,modelo,proc,ram,ssd,preco) -> None:
        self.marca = marca
        
        self.proc = proc
        self.ram = ram
        self.ssd = ssd
        self.preco = preco

    def get_marca(self):
        print(self.marca)

    def set_marca(self,new):
        self.marca = new

    def set_preco(self,valor):
        if valor > 0:
            self.preco = valor
        else:
            print('valor não pode ser negativo')

computer = Computador('ASSUS','Core i7','16GB','240GB',4999)
computer.get_marca()
computer.set_marca('Positivo')
computer.set_marca()
computer.set_preco()

    
