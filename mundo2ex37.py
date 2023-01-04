print('Exercício Número 37')

while True:
    n = int(input('Digite um número: '))
    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m','\033[m'))
    print('[1]{} Binário{}'.format('\033[0;37m','\033[m'))
    print('[2]{} Octal{}'.format('\033[0;33m','\033[m'))
    print('[3]{} Hexadecimal{}'.format('\033[0;30m','\033[m'))
    print('[x] {}Sair{}'.format('\033[0;31m','\033[m'))
    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))

    perguntanum = str(input('Digite a opção que deseja converter: '))
    if perguntanum == 'x'or perguntanum == 'X':
        break
    elif perguntanum == '1' or perguntanum == '2' or perguntanum == '3':
        if perguntanum == '1':
            potato = 'BINÁRIO'
            comp = bin(n)
            print(f'{n} convertido para {potato} fica {comp.replace("0b", "")}')
        elif perguntanum == '2':
            potato = 'OCTAL'
            comp = oct(n)
            print(f'{n} convertido para OCTAL fica {comp.replace("0o", "")}')

        elif perguntanum == '3':
            comp = hex(n)
            print(f'{n} convertido para HEXADECIMAL fica {comp.replace("0x", "")}')

    else:
        print('Opção invalida, por favor tentar novamente!')