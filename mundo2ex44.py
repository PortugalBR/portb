print("{}Exercício Número{} {}44{}".format('\033[0;31m','\033[m','\033[4;37m','\033[m'))

while True:
    n = int(input('Digite o valor do produto: '))
    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m','\033[m'))
    print('[1]{} dinheiro/cheque {}'.format('\033[0;37m','\033[m'))
    print('[2]{} á vista no cartão {}'.format('\033[0;33m','\033[m'))
    print('[3]{} 2x no cartão {}'.format('\033[0;30m','\033[m'))
    print('[4]{} 3x ou mais no cartão {}'.format('\033[0;30m', '\033[m'))
    print('[x] {}Sair{}'.format('\033[0;31m','\033[m'))
    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))

    perguntanum = str(input('Digite a opção que deseja converter: '))
    if perguntanum == 'x'or perguntanum == 'X':
        break
    elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3'or perguntanum =='4':
        if perguntanum == '1':
            ria = (n*10)/100
            rio = n-ria
            print('o seu desconto será de 10% {}, e o valor será {}.'.format(ria,rio))
        elif perguntanum == '2':
            cta = (n*5)/100
            cto = n-cta
            print('O seu desconto será de 5% {}, e o valor será {}.'.format(cta,cto))

        elif perguntanum == '3':
            print('O valor a ser pago é {}.'.format(n))

        elif perguntanum == '4':
             k = (n*20)/100
             l = n + k
             print('O seu juros será de 20% total {}.'.format(l))

    else:
        print('Opção invalida, por favor tentar novamente!')

saida = input("\nDigite {}ENTER{} para sair...".format('\033[4;33m', '\033[m'))