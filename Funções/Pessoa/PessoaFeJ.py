from Pessoa import*

class PessoaFisica():
    def __init__(self,CPF) -> None:
        self.CPF = CPF

    def get_RG(self):
        print('Número do RG é 213.5445')

Pessoa1 = PessoaFisica(105411604)
Pessoa1.get_RG()

class PessoaJuridica():
    def __init__(self,CNPJ) -> None:
        self.CNPJ = CNPJ

    def get_CNPJ(self):
        print('Cadastro Nacional de Pessoa Jurídica')

Pessoa2 = PessoaJuridica('Cadastro Nacional de Pessoa Jurídica')
Pessoa2.get_CNPJ()
        
        
