#variaveis
ask = cont = soma = 0
ask = int(input(print('Digite um numero [999 para parar]: ')).strip())
while ask != 999:

    soma += ask
    cont += 1
    ask = int(input(print('Digite um numero [999 para parar]: ')).strip())

print(f'Você digitou {cont} e a soma entre eles foi {soma}')
print('Fim')
