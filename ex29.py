print('Exercicio numero 29')
print('você esta dirigindo, quanto é a velocidade que você está dirigindo')
velocidade = float(input('Qual é a velocidade atual do carro :'))
if velocidade>80:
    print('Multado! Você exedeu o limite permitido que é de 80km/h')
    multa=(velocidade-80)*7
    print('Você deve pagar uma multa de {:.2f}!'.format(multa))

print('tenha um bom dia! Dirija com segurança!')