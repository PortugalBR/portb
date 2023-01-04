import random
from time import sleep

print('O computador escolhera um numero entre 0 e 5 se você acertar o numero você ganha, se errar você perde!')
x =random.randint(0,5)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5. Tente advinhar')
print('-=-'*20)
n= int(input('digite um numero entre 0 e 5 : '))

print('Processando...')
sleep(2)
if n == x:
    print('Parabens você conseguiu me vencer o numero era {}!! Genio(a)'.format(x))
else :
    print('Ganhei! Eu pensei no número {} e não no número {}!'.format(x,n))

