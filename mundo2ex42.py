from time import sleep

print("{}Exercício Número{} {}42{}".format('\033[0;31m','\033[m','\033[4;37m','\033[m'))
print('Preciso de 3 medidas para saber se formam um triangulo.')
a = float(input("Lado a = "))
b = float(input("Lado b = "))
c = float(input("Lado c = "))
print('calculando qual o tipo de triangulo pode ser formado...')
sleep(2)
if (a < b + c and b < a + c and c < b + c):
    if (a == b and b == c):
        print("\nOs lados formam um Triângulo Equilátero.")
    else:
        if (a == b or a == c or b == c):
            print("\nOs lados formam um Triângulo Isósceles.")
        else:#dica do professor (a !=(diferente) b != c !=a:
            print("\nOs lados formam um Triângulo Escaleno.")
else:
    print("\nOs lados não formam um triângulo!")

saida = input("\nDigite ENTER para sair...")
print('-=-'*20)