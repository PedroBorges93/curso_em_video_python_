import random as rd

um = input('Digite o primeiro nome: ')
dois = input(' Digite o segundo nome: ')
tres = input(' Digite o terceiro nome: ')
quatro = input('Digite o quarto nome: ')
lista = [um,dois,tres,quatro]
rd.shuffle(lista)
print('A ordem de apresentacao sera {}'.format(lista))
