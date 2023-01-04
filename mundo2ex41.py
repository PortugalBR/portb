from time import sleep

print("{}Exercício Número{} {}41{}".format('\033[0;31m','\033[m','\033[4;37m','\033[m'))
sleep(1)
print('\033[1;30m-=-'*30)
print('Bem Vindo a -{Confederação de Natação}- caro Estudante ! '.center(100))
print('\033[1;30m-=-\033[m'*30)
print('\n')
k= int(input('Qual a sua data de nascimento: '))
print('Analisando em qual categoria você se enquadra...')
sleep(1)
print('...')
sleep(2)
j = (k -2022)*-1

if j <= 9:
    print('Você nasceu em {} e sua categoria é MIRIM.'.format(k,'\033[31m', '\033[m',))
elif j <= 14:
    print('Você nasceu em {} e sua categoria é INFANTIL'.format(k))
elif j <= 19:
    print('você nasceu em {} e sua categoria é JUNIOR.'.format(k))
elif j <= 20:
    print('você nasceu em {} e sua categoria é SENIOR.'.format(k))
elif j >= 21:
    print('Você nasceu em {} e sua categoria é MASTER.'.format(k))

    print('[x]{}Sair{}[x]'.format('\033[4;31m', '\033[m'))

saida = input("\nDigite {}ENTER{} para sair...".format('\033[4;33m', '\033[m'))