#fase 12
#if elif elif else

print('{} Exercic de treino !{}'.format('\033[0;34m','\033[m'))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

nome= str(input('Qual é o seu {} nome :{}'.format('\033[1;35m','\033[m'))).upper()
if nome == 'BRUNO':
    print('Que nome lindão!!')
elif nome == 'AMANDA' or nome == 'JOÃO' or nome == 'PAULO' :
    print('Seu nome é bem popular no Brasil!')
elif nome in 'ANA CLÁUDIA VERA JULIANA MARIA ':
    print('Que belo nome feminino !')
else :
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {} {}!{}'.format('\033[4;30m',nome,'\033[m'))

