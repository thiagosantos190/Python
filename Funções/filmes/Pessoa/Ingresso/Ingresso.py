class Ingresso:
    def __init__(self,Preco,Setor) -> None:
        super().__init__(Preco,Setor)

    def Set_AlterarPreco(self,NovoPreco):
        self.Preco = NovoPreco

    def get_Preco(self):
        print('o Preço do Ingresso Custa R$10,00')

    def get_MostrarSetor(self):
        print('Aqui é o Setor A do Cinema')

Ingresso1 = Ingresso(10,'Setor A',3453)
Ingresso1.get_MostrarSetor()





    
        