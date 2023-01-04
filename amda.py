print('calcular')
n = int(input('digite um numero :'))
n1 = int(input('digite outro numero:'))
s =n+n1
sub = n-n1
m = n*n1
divi = n/n1
poten = n**n1
print('o resultado é = {}'.format(s))
print('o resultado da subtração é : {}'.format(sub))
print('o resultado da multiplicação é : {}'.format(m))
print('o resultado da divisão é : {}'.format(divi))
print('o resultado da potencia é : {} '.format(poten))

print('depois da calculadora farei agora o antecessor e seu sucessor.')
print('usaremos qual numero para essa operação:')
ca = (int(input('digite o numero que deseja:')))
antece = ca-1
suce = ca+1
print('o resultado do antecessor é : {} é sucessor do numero escolhido é : {}'.format(antece, suce,))


print('agora para dobro do numero escolhido, triplo e raiz quadrada ')
k = int(input('escolha o numero para o teste acima:'))
dobro = k*2
print('o resultado dobro é : {}'.format(dobro))
triplo = k*3
print('o resultado triplo é: {}'.format(triplo))
raiz = float(input('Entre com o valor: '))
raizQ = raiz ** (1/2)
raizC = raiz ** (1/3)
print('A raiz quadrada foi {:.3f} e a raiz cúbica foi {:.3f}'.format(raizQ, raizC))
