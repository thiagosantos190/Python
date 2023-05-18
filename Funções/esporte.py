class Jogador:
    def __init__(self,nome,posicao,numero,altura,peso) -> None:
        self.nome = nome
        self.posicao = posicao
        self.numero = numero
        self.altura = altura
        self.peso = peso

    def get_nome(self):
        print(self.nome)

    def get_peso(self):
        print(self.peso)

    def set_numero(self):
        print(self.numero)

    def get_numero(self):
        print(self.numero)

    def get_altura(self):
        print(self.altura)

jog = Jogador('Neimar','Atacante',10,'1.70',75)

jog2 = Jogador('Messi','Atacante',10,'1.99',70)

jog.get_nome()
jog.get_numero()
jog.get_altura()

jog2.get_nome()
jog2.get_numero()
jog2.get_peso()
jog2.get_numero()
jog2.get_altura()




    
