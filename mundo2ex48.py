s = 0
cont = 0
for n in range(1,501):
    if n % 3 == 0:

        print(n)

    s += n
    cont += 1

print('A somatoria dos numeros {} é :{:.2f}'.format(cont, s))



