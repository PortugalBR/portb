r = int(input('qual o numero : '))
n = int(input('qual a razão : '))
x = r + (10 -1) * n
for c in range(r, x + n, n ):


    print('{}'.format(c), end=' ->')

print('ACABOU!')