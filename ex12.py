import random
print('018 sorteio com nome')
k= str(input('digite o nome: '))
l = str(input('digite outro nome: '))
q = str(input('digite outro nome: '))
s = str(input('digite o ultimo nome: '))
lista = [k, l, q, s]
escolhido = random.choice(lista)
print('O jovem sorteado é o : {} '.format(escolhido))
