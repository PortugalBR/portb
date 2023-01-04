sexo = str(input('Digite o sexo da pessoa [M/F] : ')).strip().upper()[0]
while not sexo in 'MmFf':
    print('Opção invalida digite [M]para masculino e [F] para feminino')
    sexo = str(input('Digite novamente: [M/F] ')).strip().upper()[0]
print('Acabou')

