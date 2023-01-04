print('=' * 10, 'desafio 60', '=' * 10)
from math import factorial
nf = int(input('Digite um número para saber seu fatoria: '))
fat = factorial(nf)
print(f'O fatorial de {nf} é {fat}.')


#ou

n = float(input('Digite um número para calcular o seu fatorial: '))
fatorial = 1
while n - 1 != 0:
    fatorial *= n
    n -= 1
print(f'{n}! = {fatorial}.')

#or

fat = int(input('Digite um número para saber seu fatorial: '))
fatorial = 1
for f in range(1, fat+1,):
    fatorial *= f
print(fatorial)