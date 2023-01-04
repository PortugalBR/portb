from random import randint
from time import sleep

print("{}Exercício Número{} {}45{}".format('\033[0;31m','\033[m','\033[4;37m','\033[m'))
print('JO KEN PÔ')
print('Pedra, papel ou tesooura!')

print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))
n = str(input('Você ja jogou ? '))
if n == 'sim' or n=='Sim' or n=='SIM' or n== 'SIm':
    print('vamos lá então!')
elif n != 'sim':
    print('''No Janken-pon, os jogadores devem simultaneamente esticar a mão, na qual cada um formou um símbolo (que significa pedra, papel ou tesoura).\nEntão, os jogadores comparam os símbolos para decidir quem ganhou, da seguinte forma:

Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).''')
while True:
    jokenpo = ('Pedra', 'Papel', 'tesoura')
    computador = randint(0, 2)

    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m','\033[m'))
    print('[ 0 ]{} PEDRA {}'.format('\033[0;37m','\033[m'))
    print('[ 1 ]{} PAPEL {}'.format('\033[0;33m','\033[m'))
    print('[ 2 ]{} TESOURA {}'.format('\033[0;30m','\033[m'))
    print('[ x ] {}Sair{}[ x ]'.format('\033[0;31m','\033[m'))
    print('{}-=-=-=-=-=-=-=-=-=-=-=-=-{}'.format('\033[31m', '\033[m'))

    print('-=-'*20)
    jogador = int(input('Qual a sua jogada ? '))
    print('JO')
    print('KENNN')
    sleep(1)
    print('PO')
    print('-=-' * 20)
    sleep(1)
    if jogador == 'x' or jogador == 'X':
        break
    elif computador == 0: #computador jogou pedra
        if jogador == 0: #jogador jogou pedra
            print('Você escolheu {} eu escolhi {}.deu empate(0)'.format(jogador,jokenpo[computador],))
        elif jogador == 1: #papel
            print('Papel')
            print('Você escolheu {} eu escolhi {}.(0)'.format(jogador,jokenpo[computador],))
        elif jogador == 2:#tesoura
            print('Tesoura.')
            print('Você escolheu {} eu escolhi {}.(0)'.format(jogador,jokenpo[computador],))
        else :
            print('Invalido')
        print('-=-' * 20)
    elif computador == 1 : #computador jogou papel
        if jogador == 0 : #jogador jogou papel
            print('Você escolheu {} eu escolhi {}..'.format(jogador,jokenpo[computador]))
            print('Empate,na proxima eu ganho de você !(1)')
        elif jogador == 1 :#pedra
            print('Você escolheu {} eu escolhi {}.(0)'.format(jogador,jokenpo[computador],))
        elif jogador == 2 :#tesoura
            print('Papel')
            print('Você escolheu {} eu escolhi {}.!(1)'.format(jogador,jokenpo[computador],))
        print('-=-'*20)
    elif computador == 2 : #computador jogou tesoura
        if jogador == 0 :#jogador jogou tesoura
            print('Tesoura!')
            print('Você escolheu {} eu escolhi {}.(0)'.format(jogador,jokenpo[computador],))
        elif jogador == 1 : #papel
            print('Você escolheu {} eu escolhi {}.(0)'.format(jogador,jokenpo[computador],))
        elif jogador == 2 : #pedra
            print('Você escolheu {} eu escolhi {}.(0)'.format(jogador,jokenpo[computador],))
            print('Eu escolho Pedra,empate? tudo bem eu perdi.')
        print('-=-'*20)
    else:
        print('Opção invalida, por favor tentar novamente!(2)')
