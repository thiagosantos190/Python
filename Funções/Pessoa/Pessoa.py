class Pessoa:
    def __init__(self,Nome,Telefone,Email,Endereco) -> None:
        self.Nome = Nome
        self.Telefone = Telefone
        self.Email = Email
        self.Endereco = Endereco

    def get_negociar(self):
        print('Ótimo Negócio')

Person = Pessoa('Lucas',999123321,'Email@gmail.com','Rua Serra Azul 15')
Person.get_negociar()

