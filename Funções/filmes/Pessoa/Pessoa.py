class Pessoa:
    def __init__(self,Matricula,Nome,Idade) -> None:
        super().__init__(Matricula,Nome,Idade)

class Aluno:
    def __init__(self,Matricula,Nome,Idade,Nota1,Nota2,Lecionar) -> None:
        self.Matricula = Matricula
        self.Nome = Nome
        self.Idade = Idade
        self.Nota1 = Nota1
        self.Nota2 = Nota2
        self.Media = 0
        self.Lecionar = Lecionar

    def get_CalcularMedia(self):
        self.Media = self.Nota1+self.Nota2/2
        print(f'Sua Média das Notas é {self.Media}')

    def get_Estudar(self):
        print('Estou Estudando')


aluno1 = Aluno(1234,'João',12,6,7,'dar Aula')
aluno1.get_CalcularMedia()
aluno1.get_Estudar()

        

    

    
        