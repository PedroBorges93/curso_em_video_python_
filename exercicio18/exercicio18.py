import math as mt

an = float(input('Digite um numero: '))
s = mt.sin(mt.radians(an))
c = mt.cos(mt.radians(an))
t = mt.tan(mt.radians(an))
print('O angulo de grau : {}\nSENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}'.format(an, s, c, t))
