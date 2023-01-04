


while True:

    print('>>>Preciso de 2 números para compara-los<<<')
    um = int(input('Digite um número: '))
    dos = int(input('Digite outro número: '))

    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m','\033[m'))
    print('{}[1] somar{}'.format('\033[0;37m','\033[m'))
    print('{}[2] multiplicar{}'.format('\033[0;33m','\033[m'))
    print('{}[3] maior{}'.format('\033[0;32m','\033[m'))
    print('{}[4] novos números{}'.format('\033[0;35m', '\033[m'))
    print('{}[X] Sair{}'.format('\033[0;31m','\033[m'))
    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))

    perguntanum = str(input('Digite a opção que deseja converter: ')).upper()
    if perguntanum == 'x'or perguntanum == 'X':
        print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))
        break

         #apertar 1
    elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3' or perguntanum == '4':
        if perguntanum == '1':
            produto =  um + dos
            print(f'O valor ({produto}) é o Resultado entre ({um}) e ({dos}) .')
            print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))

            #apertar 2
        elif perguntanum == '2':
            produto = um * dos
            print(f'{produto} é o resultado entre {um} e {dos} .')
            print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))

            #apertar 3
        elif perguntanum == '3':
            if um > dos:
                print(f'O numero {um} é o maior.')
            if dos > um:
                print(f'O numero {dos} é maior.')
            elif um == dos:
                print('os numeros são Iguais. ')
                print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))

        elif perguntanum == '4':
            print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))
            print('>>>Vamos lá preciso de 2 numeros<<<')
            #novo tudo
            tres = int(input('Digite um número: '))
            quatro = int(input('Digite outro número: '))

            print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))
            print('{}[1] somar{}'.format('\033[0;37m', '\033[m'))
            print('{}[2] multiplicar{}'.format('\033[0;33m', '\033[m'))
            print('{}[3] maior{}'.format('\033[0;32m', '\033[m'))
            print('{}[4] novos números{}'.format('\033[0;35m', '\033[m'))
            print('{}[X] Sair{}'.format('\033[0;31m', '\033[m'))
            print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))

            perguntanum = str(input('Digite a opção que deseja converter: ')).upper()
            if perguntanum == 'x' or perguntanum == 'X':
                print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))
                break

                # apertar 1
            elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3' or perguntanum == '4':
                if perguntanum == '1':
                    potato = tres + quatro
                    print(f'O valor ({potato}) é o Resultado entra ({tres}) e ({quatro}) .')
                    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))

                    # apertar 2
                elif perguntanum == '2':
                    potato = tres * quatro
                    print(f'{potato} é o resultado entre {tres} e {quatro} .')
                    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))

                    # apertar 3
                elif perguntanum == '3':
                    if tres > quatro:
                        print(f'O numero {tres} é o maior.')
                    if quatro > tres:
                        print(f'O numero {quatro} é maior.')
                    elif quatro == tres:
                        print('os numeros são Iguais. ')
                        print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))

                elif perguntanum == '4':
                    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[30m', '\033[m'))

    else:
        print('Opção invalida, por favor tentar novamente!')