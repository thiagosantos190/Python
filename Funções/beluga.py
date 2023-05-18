class People:
    def __init__(self,nome,idade) -> None:
        self.__nome = nome
        self.idade = idade

    def get_nome(self):
        return self.__nome
    
    def set_nome(self,name):
        self.__nome = name
    
pes1 = People('Luiz',20)
pes1.set_nome('thays')
print(pes1.get_nome())
pes1.idade = 28
print(pes1.idade)