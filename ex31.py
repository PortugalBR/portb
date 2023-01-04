from time import sleep

print('Exercicio numero 31')
print('Calculando o valor da viagem por Kilometros,')
valor = float(input('Por favor digite,qual a distancia da sua viagem em kilometros: '))
print('Calculando aguarde..., (você sabia que esse computador processa cerca de 3,6gigas de documentos em 1 seg)ou seja já calculei' )
sleep(3)
var = (1/2)
vari =(45/100)
if valor<=200:
    print('O valor será de {:.2f}R$.'.format(valor*var))
else :
    print('O valor será de {:.2f}R$.'.format(valor*vari))
print('Boa viagem!,Bon voyage!,auf wiedersen,tchuss,ciao,have a good trip!')