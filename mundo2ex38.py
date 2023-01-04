print("{}Exercício Número {}38{}".format('\033[0;31m','\033[m','\033[m'))
print('Comparando números...')
print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))
numerum= str(input('Qual o primeiro número :'))
numerdois= str(input('Qual o segundo número :'))
print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))

if numerum > numerdois:
    print('O primeiro valor é maior {}.'.format(numerum))
elif numerum < numerdois:
    print('O Segundo numero é maior {}.'.format(numerdois))
elif numerum == numerdois:
    print('Não existe maior, os dois são iguais.'.format(numerum,numerdois))

print('{}Sair{}'.format('\033[4;33m', '\033[m'))


print('[x] {}Sair{} [x]'.format('\033[4;33m','\033[m'))
saida = input("\nDigite {}ENTER{} para sair...".format('\033[4;33m', '\033[m'))
