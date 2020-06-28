import math as mt
cata = float(input('Digite o valor do cateto maior: '))
catb = float(input('Digite o valor do cateto menor: '))
hip = mt.hypot(cata,catb)
print ('O valor de hypotenusa de {}, e {} e igual a {:.2f}'.format(cata,catb,hip))
print ('Hipotenusa {:.2f}'.format((cata**2+catb**2)**(1/2)))
