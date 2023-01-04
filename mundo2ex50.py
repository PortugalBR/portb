import pytz as pytz


soma = 0
conta = 0

for aa in range(0,6):
    a = int(input('Qual é o numero:'))

    if a %2 == 0:
        soma += a
        conta += 1
        print(a)

    elif a %3 != 0:
        print("o valor não é par")




print('Você informou {} números pares e a soma é {}.'.format(conta, soma))

from datetime import date

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')

print(data_em_texto)

