class Funcionário:
    def __init__(self,Nome,Matricula,Salario,Ponto) -> None:
        self.Lista = []
        self.Nome = Nome
        self.Matricula = Matricula
        self.Salario = Salario
        self.Ponto = Ponto

    def get_BatePonto(self):
        self.Ponto = int(input('Digite 0 Para Falta e 1 Para Presença '))
        if self.Ponto==0:
            print('Lista de Falta')
            self.get_BatePonto.append
        else:
            print('Lista de Presença')
            
       

Funcionário1 = Funcionário('Carlos',1234,2500,0)
Funcionário1.get_BatePonto()

        




            
