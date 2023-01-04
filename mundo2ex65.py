n = int(input("Digite um numero inteiro:"))
opcao = str(input('Quer continuar?\n'
                  '(Digite "S" para continuar, Digite "N" para encerrar) :')).strip().upper()
contagem = 0
soma = n
if n != 0:
    contagem = 1
if opcao != "S" and opcao != "N":
    print("Opcao inválida, Progama Rodando...")
    opcao = "S"
maior = menor = n
while opcao == 'S':
    n = int(input("Digite um numero inteiro:"))
    opcao = str(input('Quer continuar? \n'
                      '(Digite "S" para continuar, Digite "N" para encerrar) :')).strip().upper()
    if opcao != "S" and opcao != "N":
        print('Opção inválida, Progama Rodando...')
        opcao = "S"
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    if n != 0:
        contagem += 1
media = soma / contagem
print(20 * "_")
print(f"O maior valor é : {maior}\n"
      f"O menor valor é : {menor}\n"
      f"A Média entre os numero é : {media}")
print('Progama encerrado')

#refazer