nome = str(input('Digite seu nome: ')).strip()
if nome.upper() == 'PEDRO':
    print ('Que nome lindo voce tem!')
else:
    print('Bom dia {}!'.format(nome))