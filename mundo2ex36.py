from time import sleep

print('{}Exercício Numero 36 Mundo 2{}'.format('\033[4;31m','\033[m'))
casa = int(input('Qual o valor da casa :'))
sleep(1)
salario = int(input('Qual é o seu salario :'))
sleep(1)
tempo = int(input('Você quer pagar em quantos anos :'))
sleep(1)
a = 30
s = (salario*a/100)#30porcento do salario
b = tempo*12 #parcelas a pagar(numero de parcelas no valor c )
c = casa/b #valor total da casa dividido pelas parcelas     (valor a pagar por mes)
 #resultado se o valor da para ser pago mensalmente pelo salario

if c <= s :
    print('Você pode pagar {:.2f}!'.format(c))
elif c == s:
    print('você pode pagar exatamente {:.2f}! '.format(s))
else :
    print('Você nao pode pagar! Você tem {:.2f} e o valor seria {} mensalmente !'.format(s,c))
sleep(5)

print(c,b,s,)