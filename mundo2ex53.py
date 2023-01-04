string = input('Qual a frase :')
stringSemEspacos = string.replace(' ', '')
stringTodaMinuscula = stringSemEspacos.lower()
stringInvertida = stringTodaMinuscula[::-1]
if stringInvertida == stringTodaMinuscula:
    print ("SIM")
else:
    print ("NAO")

print('-=-'*30)

string = input('qual a palavra :')
stringSemEspacos = string.replace(' ', '')
stringTodaMinuscula = stringSemEspacos.lower()
stringInvertida = stringTodaMinuscula[::-1]
if stringInvertida == stringTodaMinuscula:
    print ("SIM")
else:
    print ("NAO")