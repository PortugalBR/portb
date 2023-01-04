cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('{} Exercício número 2'.format(cores['amarelo']))
a = input ('digite algo: ')
print('O tipo primitivo desse valor é ',type(a))
print('Só tem espaços :', a.isspace())
print('É um número:' , a.isnumeric())
print('É alfabético:', a.isalpha())
print('Está em maiúsculas :', a.isupper())
print('Está em minúsculas :', a.islower())


