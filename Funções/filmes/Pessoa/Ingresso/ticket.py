

class IngressoVip:
    def __init__(self,Camarote,OpenBar,OpenFood,Estacionamento) -> None:
          self.Camarote = Camarote
          self.OpenBar = OpenBar
          self.OpenFood = OpenFood
          self.Estacionamento = Estacionamento

    def get_PegarBebida(self):
         print('Estou bebendo um Suco de limão')

    def get_AcessarCamarote(self):
         print('Estou Entrando no Camarote')

Ingresso1 = IngressoVip('Camarote','OpenBar','OpenFood','Estacionamento')
Ingresso1.get_PegarBebida()
Ingresso1.get_AcessarCamarote()
