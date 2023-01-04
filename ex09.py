a = float(input('quantos kilometros você andou : '))
b = int(input('quantos dias o carro você permaneceu com o veiculo : '))
c = 60*b
d = 0.15*a
e = c + d
print('O valor total a pagar em kms = {:.2f} R$ , e o valor a pagar por dias é = {:.2f} R$.'.format(d , c))
print('O valor total a ser pago será : {:.2f} R$.'.format(e))