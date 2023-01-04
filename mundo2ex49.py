t= int(input('Digite um número para saber sua tabuada:'))

print('_'*15)

for tab in range(1,11) :
   print(f'\n{t}x{tab} = {t*tab}')