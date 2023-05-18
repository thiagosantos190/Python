from person import Pessoa
from contador import Contador

cont = Contador()
lista = []

while True:
    nome = input('digite seu Nome ')
    idade = int(input('digite sua idade '))
    pessoa = Pessoa(nome,idade)
    lista.append(pessoa)
    cont.increment()
    
    op = input('deseja continuar S/N? ').upper()
    if op == 'N':
        break

for pes in lista:
    print(pes.nome,pes.idade)


