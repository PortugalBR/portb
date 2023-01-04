from time import sleep

print("{}Exercício Número {}39{}".format('\033[0;31m','\033[m','\033[m'))
print('Alistamento...')
print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))
numerum= int(input('Data do seu nascimento :'))
print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))
sleep(3)
x = (numerum -2004)*-1
if numerum < 2004:
    print('Você nasceu em {} e {}passou do tempo{} se alistar em {} ano(s).'.format(numerum,'\033[31m', '\033[m',x))
elif numerum > 2004:
    print('Você nasceu em {}ainda vai se alistar.'.format(numerum))
elif numerum == 2004:
    print('você nasceu em {} e precisa vai se alistar.'.format(numerum))
else:
    print('Opção invalida!')
    print('{}Sair{}'.format('\033[4;33m', '\033[m'))







#professor forma muito diferente.


from datetime import date
atual = date.today().year
nasce= int(input('Ano de nascimento :'))
idade = atual - nasce
pritnt( nasce,idade, atual)
if idade == 18:
    saldo = 18 - idade
    print(alistar)
elif idade< 18:
    saldo = idade -18
    print('ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('seu alistamento será em {}'.format(ano))
elif idade >18:
    saldo = idade -18
    print( saldo)
    print('voce deveria ter se alistado a{}'.format(saldo))
    ano = atual -18
    print('seu alistamento foi em {}'.format(ano))

    print('falta anos {}'.format(saldo))

print('[x] {}Sair{} [x]'.format('\033[4;33m','\033[m'))
saida = input("\nDigite {}ENTER{} para sair...".format('\033[4;33m', '\033[m'))