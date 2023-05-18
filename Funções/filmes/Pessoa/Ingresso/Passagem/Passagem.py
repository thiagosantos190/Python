class Passagem:
    def __init__(self,Preco,Assento) -> None:
       self.Preco = Preco
       self.Assento = Assento

    def set_AlterarPreco(self,NovoPreco):
        self.Preco = NovoPreco

    def get_Preco(self):
        print('O Preço da Passagem é R$5,00')

    def get_Assento(self):
        print(f'O Assento Escolhido foi {self.Assento}')

Passagem1 = Passagem(315,55)
Passagem1.get_Assento()
Passagem1.set_AlterarPreco(10)
Passagem1.get_Preco()


