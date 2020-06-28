d = int(input('Digite quantos dias voce ficou com o carro: '))
k = float(input('Digite quantos quilometros voce rodou com o carro: '))
td= d*60
tk =float( k * 0.15)
tt=td+tk
print('O valor a ser pago por usar {}  dias foi {}, e ter rodado {} km foi {} , O total a ser pago e de {} reais'.format(d,td,k,tk,tt))
