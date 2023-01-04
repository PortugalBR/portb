from time import sleep

print("{}Exercício Número{} {}43{}".format('\033[0;31m','\033[m','\033[4;37m','\033[m'))
sleep(1)
print('\033[1;30m-=-'*30)
print('CALCULADORA de \033[1;33mIMC\033[m \033[1;30m(indice de massa corporea)!\033[m '.center(100))
print('\033[1;30m-=-\033[m'*30)
print('\n')
k = float(input('Qual a seu peso(somente numeros sem virgula): '))
l = float(input('Qual a sua altura(ex:1,90): '))
print('Analisando em qual categoria você se enquadra...')
sleep(1)
print('...')
sleep(2)
j = k/(l*l)#(altura **2) dica prof
if j <= 18.5:
    print('Você tem um imc de {:.2f} e sua categoria é abaixo do peso.'.format(j,'\033[31m', '\033[m',))
elif j <= 25:
    print('Você tem um imc de {:.2f} e sua categoria é peso ideal.'.format(k))
elif j <= 30:
    print('você tem um imc de {:.2f} e sua categoria é sobrepeso.'.format(k))
elif j <= 40:
    print('você tem um imc de {:.2f} e sua categoria é obesidade.'.format(k))
elif j >= 41:
    print('Você tem um imc de {:.2f} e sua categoria é obesidade mórbida.'.format(k))

    print('[x]{}Sair{}[x]'.format('\033[4;31m', '\033[m'))

saida = input("\nDigite {}ENTER{} para sair...".format('\033[4;33m', '\033[m'))
