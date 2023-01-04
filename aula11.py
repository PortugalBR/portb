print(\033[0;33;44m
\033[0;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7:30m  #cores da aula 11
)
print('\033[1;31;43ola mundo !\033[m')

nome = 'bruno'
print('ola muito prazer em te conhecer{} {} {}!!!'.format('\033[4;34m', nome,'\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('ola muito prazer em te conhecer{} {} {}!!!'.format(cores['amarelo'], nome,cores['limpa']))

#style [0 1 4 7] 4 sublinha 7 negativo (inverso)
#text [30 ate 37] cada uma é uma cor diferente, branco, vermelho, verde,amarelo, azul,roxo ,azul,cinza
#back [40 ate 47] fundo das palavras nas mesmas cores do texto