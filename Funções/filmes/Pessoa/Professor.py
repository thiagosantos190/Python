from Pessoa import*
class Professor:
    def __init__(self,Formacao,Disciplina,CargaHoraria,Salario) -> None:
        self.Formacao = Formacao
        self.Disciplina = Disciplina
        self.CargaHoraria = CargaHoraria
        self.Salario = Salario

    def get_Lecionar(self):
        print('Estou Dando Aula Nesse Momento')

Professor1 = Professor('Graduado em Matemática','Matematica',20,3000)
Professor1.get_Lecionar()

        