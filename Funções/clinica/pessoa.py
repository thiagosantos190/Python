class Pessoa:
    def __init__(self,nome,telefone) -> None:
        self.nome = nome
        self.telefone = telefone

    def falar(self):
        print(f'{self.nome} FALOU')


class Veterinario(Pessoa):
    pass
class Cliente(Pessoa):
    pass
vet = Veterinario('joão silva',88888888)
vet.falar()

cli = Cliente('APARECIDO SOUZA',77777)
cli.falar()