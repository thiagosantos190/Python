class Pessoa:
    def __init__(self,nome,idade,endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def get_nome(self):
        print(self.nome)

    def set_idade(self,novaIdade):
        self.idade = novaIdade

    def get_endereco(self):
        print(self.endereco)

    def get_idade(self):
        print(self.idade)
    
pessoa1 = Pessoa('Thiago',19,'Rua Serra')
pessoa1.get_nome()
pessoa1.set_idade(18)
pessoa1.get_idade()
pessoa1.get_endereco()
