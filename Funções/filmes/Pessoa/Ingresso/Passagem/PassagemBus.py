from Passagem import*

class PassagemAvião(Passagem):
    def __init__(self,PortaDeEmbarque) -> None:
        
        self.PortaDeEmbarque = PortaDeEmbarque
        

    def get_Decolar(self):
        print('O Avião Está Decolando')

Passagem2 = PassagemAvião('O Avião Está Decolando')
Passagem2.get_Decolar()


class PassagemBus(Passagem):
    pass

    def get_Abastecer(self):
        print('Abastecendo o Bus')

Passagem3 = PassagemBus(400,'O Assento Escolhido foi','Abastecendo o Bus')
Passagem3.get_Assento()
Passagem3.get_Abastecer()
Passagem3.Decolar()
