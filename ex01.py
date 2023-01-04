from time import sleep

print('Exercicio numero 1')
n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
s = n1 + n2
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('')
print('{}-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'.format(cores['azul']))
sleep(3)
print( '{}A soma do numero ', n1,'e', n2,'é =', s )
print('{}-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'.format(cores['azul']))
sleep(3)
print('A soma entre{} {}  e {}  = {} {}'.format(cores['limpa'],n1, n2, s,cores['amarelo']))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
sleep(3)
nome = input('comment tu apelle:'.format('\033[m'))
print('Parabéns{} {} {} pelo seu belissimo trabalho !'.format(cores['azul'],nome,cores['amarelo'] ))

