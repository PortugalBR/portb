from time import sleep

print("{}Exercício Número {}40{}".format('\033[0;31m','\033[m','\033[m'))
print('Amanda linda fez comigo esse lindissimo desafio !')
sleep(1)
numerum= int(input('Nota número 1 :'))
numerdos= int(input('Nota número 2:'))
j = (numerum+numerdos)/2
if j < 5.0:
    print('{}REPROVADO!{}Boa sorte na proxima!'.format('\033[0;31m','\033[m'))
elif 7 > j >=5:
    print('{}RECUPERAÇÃO!{}Estude mais !'.format('\033[0;33m','\033[m'))
elif j > 7.0:
    print('{}APROVADO!{} PARABENS!'.format('\033[0;32m','\033[m'))
else :
    print('Somente números!')
print(j)

saida = input("\nDigite {}ENTER{} para sair...".format('\033[4;33m', '\033[m'))