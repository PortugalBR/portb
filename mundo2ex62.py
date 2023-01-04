
primeiro = int(input('Primeiro termo da PA: ').strip())
razão = int(input('Razão da PA: ').strip())
termo = primeiro
cont = 1
total = 0
mais = 10
print('{}, '.format(cont), end='')
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ->',end='')
        termo += razão
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ?').strip())
print(f"Progressão finalizada com {total} termos")
print('Fim!')
