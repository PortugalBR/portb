# GRUPO DA MAIORIDADE

from time import sleep
from datetime import date

somatoria = 0
maioridade = 0
menoridade = 0
atual = date.today().year

np = int(input("Digite o número de pessoas: "))
for c in range(1, np+1):
    an = int(input("Digite o ano de nascimento: "))
    idade = atual - an
    somatoria += idade
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
sleep(0.5)

if np > 1:
    print("A somatória das idades é igual à: ", somatoria)
    sleep(0.5)

if maioridade > 1 and menoridade > 1:  # geral
    print(f"Dentre essas pessoas, {maioridade} são maiores de idade e {menoridade} são menores de idade!")
elif maioridade == 1 and menoridade > 1:
    print(f"Dentre essas pessoas, apenas {maioridade} é maior de idade e {menoridade} são menores de idade!")
elif maioridade > 1 and menoridade == 1:
    print(f"Dentre essas pessoas, {maioridade} são maiores de idade e apenas {menoridade} é menor de idade!")
elif maioridade == 1 and menoridade == 1:
    print(f"Dentre essas pessoas, {maioridade} é maior de idade e {menoridade} é menor de idade!")
elif menoridade == 0 and np > 1:
    print(f"Todas as {np} pessoas são maiores de idade!")
elif maioridade == 0 and np > 1:
    print(f"Todas as {np} pessoas são menores de idade!")
elif np == 1:
    if idade >= 21:
        print("Essa pessoa é maior de idade!")
    else:
        print("Essa pessoa é menor de idade!")
sleep(1)
print("FINALIZANDO...")
sleep(0.5)


#prof
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {} pessoa nasceu : '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1

    else:
        totmenor += 1

print('tivemos {} pessoas maiores de idade '. format(totmaior))
print('tivemos {} pessoas menores de idade '.format(totmenor))

