class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3) -> None:
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.ra = ra
        self.media = 0

    def get_mostrarSituacao(self):
        
        self.media = self.nota1+self.nota2+self.nota3/3
        if(self.media>=7):
            print('Aluno Aprovado')
        if(self.media<6.9):
            print('Exame')
        if(self.media<5):
            print('Reprovado')

aluno1 = Aluno('Lucas',1234,1,1,1)
aluno1.get_mostrarSituacao()

        
    
    