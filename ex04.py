k = int(input('escolha o numero da sua nota para calcularmos a sua media:'))
print('ja inseriu uma nota,vamos a segunda agora:')
l = int(input('escolha sua segunda nota :'))
m = k+l
n = m/2
print('o resultado da media das suas notas é: {}'.format(n))
print('obrigado por participar!')


print('ja temos o calculo das notas, mas agora ,são metros, centimetro e milimetros.')
o = float(input('qual o valor que gostaria em metros:'))
e = input('calculando...')
print('o valor escolhido foi {} metros.'.format(o))
p = o*100
print('gostaria de saber em centimentros? se não quiser somente saia.')
a = input('calculando...')
print('o resultado em centimetros é: {} centimetros.'.format(p))
c = input('agora são os milimetros, calculando...')
d = p*10
print('o resultado em milimetros para o {} metros é : {} milimetros.'.format(o,d))
