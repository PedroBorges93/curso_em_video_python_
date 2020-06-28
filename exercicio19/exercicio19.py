import random as rd

um = input('Digite o primeiro nome: ')
dois = input(' Digite o segundo nome: ')
tres = input(' Digite o terceiro nome: ')
quatro = input('Digite o quarto nome: ')
print('O Aluno escolhido para apagar o quadro foi o {}'.format(rd.choice([um,dois,tres,quatro])))
