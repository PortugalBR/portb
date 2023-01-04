import random
from time import sleep

print('O computador escolhera um numero entre 0 e 5 se você acertar o numero você ganha, se errar você perde!')
pc =random.randint(0,10)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 10. Tente advinhar')
print('-=-'*20)

tentativas = 0
acertou = False

print('Processando...')
sleep(1)

while not acertou:
    jogador= int(input('digite um numero entre 0 e 10: '))
    tentativas +=1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('mais... tente mais uma vez')

        elif jogador > pc:
            print('menos... tente mais uma vez')
print(f'Acertou em {tentativas} tentativas. Parabéns!')
