print('Desafio 12')
preço = float(input('qual é o preço do produto :R$ '))
novo = preço -(preço*5/100)
print('o valor é {:.2f} e com desconto de 5% o valor ficará : {:.2f}R$'.format(preço, novo))
