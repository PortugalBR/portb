import random

print('desafio numero 016')
import math
numero = float(input('digite um numero com virgula(lembrando que a vigula e ponto !): '))
arredon = math.floor(numero)
print('o numero resultante é = {} '.format(arredon))

print('017 Calcule a Hipotenusa  no tringulo retângulo :')
co = float(input('digite o CATETO OPOSTO: '))
ca = float(input('digite o CATETO ADJACENTE: '))


print('calculando...')
coo = (co * co)
caa = (ca * ca)
hipo = coo + caa
tenusa = (hipo**(1/2))
print('O resultado da hipotenusa do cateto oposto {:.0f} e do cateto adjacente {:.0f} é igual a = {:.0f} ² ou {} .'.format( co, ca, tenusa ,hipo))

import math
print('017 Calcule a Hipotenusa  no tringulo retângulo :')
co = float(input('digite o CATETO OPOSTO: '))
ca = float(input('digite o CATETO ADJACENTE: '))
hi = math.hypot(co,ca)
print('o resultado é : {:.2f}'.format(hi))



