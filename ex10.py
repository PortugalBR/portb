import math
num = int(input('digite um numero : '))
raiz = math.sqrt (num)
print('a raiz de {} é igual a {:.2f} '.format(num, math.ceil(raiz)))

from math import sqrt, floor
num = int(input('digite um numero : '))
raiz = math.sqrt (num)
print('a raiz de {} é igual a {:.2f} '.format(num, floor(raiz)))

import random
num = random.randint( 1, 60)
print(num)

import emoji
print(emoji.emojize("olá, mundo :earth_americas: ", use_aliases='true'))

