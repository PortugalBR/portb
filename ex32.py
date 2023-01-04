from calendar import calendar, isleap
from time import sleep

print('Desafio numero 32')
print('Faça um programa que diga se o ano é bissexto.')
ano = int(input('Qual ano você gostaria de saber se é bissexto: '))
calendar
isleap(ano)
sleep(2)
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('O ano de {} é bissexto!'.format(ano))
else :
    print('O ano de {} não é bissexto!'.format(ano))
isleap(2024)