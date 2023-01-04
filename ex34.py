from time import sleep

print('Desafio numero 34')
print('-=-'*30)
salario = float(input('Qual o valor do seu salario para que eu calcule o valor do seu aumento:'))
print('-=-'*30)

print('salario é {:.2f}.'.format(salario))
print('calculando seu aumento ...')
sleep(3)
if (salario > 1250) :
    m = salario*10
    n = m/100
    print('O seu aumento será de {}'.format(n))
    o = n+salario
    print('O seu novo salario será :{}'.format(o))
else:
    m =salario*15
    n =m/100
    print('O seu aumento será de {}'.format(n))
    o = n + salario
    print('O seu novo salario será :{}'.format(o))
print('Obrigado pelo seu trabalho!.')