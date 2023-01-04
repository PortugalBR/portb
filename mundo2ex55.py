from time import sleep
from datetime import date

# Variaveis auxiliares
maior = 0
menor = 0
atual = date.today().year

# Laço de coleta e analise
print('O maior e o menor peso entre 5 pessoas')
for c in range(1, 6):
    an = float(input(f"Digite o peso da {c}º pessoa: "))
    if c == 1:
        menor = an
        maior = an
    else:
        if an > maior:
            maior = an
        if an < menor:
            menor = an

print(f'O maior peso capturado foi {maior} e o menor peso capturado {menor}')