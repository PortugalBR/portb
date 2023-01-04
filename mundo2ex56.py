from time import sleep
from datetime import date

# Variaveis auxiliares
maior = 0
menor = 0
atual = date.today().year
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

# Laço de coleta e analise
for c in range(1, 5):
    print('----------{} pessoa----------'.format(c))
    idade = int(input(f"Digite a IDADE da {c}º pessoa: "))
    nome = str(input(f'Qual o NOME da {c}º pessoa : ')).strip()
    sexo = str(input(f'qual o SEXO da {c}º pessoa [M/F]: )')).lower()
    somaidade += idade

#if do sexo masculino
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

#feminino
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

#media de idade
médiaidade = somaidade /4

print(f'o homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
print(f'a media de idade do grupo é de {médiaidade} anos ')


