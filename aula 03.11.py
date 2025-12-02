#for i in range(1,11):
#    if i == 4:
#        break
#    print('{}'.format(i))

#for i in range(1,11):
#    if i == 4:
#        continue
#    print('{}'.format(i))

#################################################################################################

#soma = 0
#
#while True:
#    numero = float(input("Digite um numero qualquer ou 0 para encerrar: \n"))
#
#    if numero == 0:
#        break
#    soma = soma + numero          
#    print(f"A soma dos numeros é: {soma}")

#################################################################################################

#for letra in "ola mundo":
#    print(letra)

#for numero in (1,2,3,4,5,6,7,8,9):
#    print(numero)

#numero = [1,2,3,4,5,6,7,8,9]
#for num in numero:
#    print(num)

#for item in range(5):
#    print("Hello World")

#################################################################################################

#numero = float(input("Digite o numero que deseja que seja feita a tabuada \n"))
#for mult in range(11):
#    resultado = numero * mult
#    print(f"{numero} X {mult} = {resultado}")

#################################################################################################

#cont = 1
#while cont <=100:
#    print(cont, end=" ")
#    cont += 1

#for cont in range(1,101):
#    print(cont, end=" ")

#################################################################################################

#nome = (str(input("Digite seu nome: ")))
#cont = (int(input("Digite quantas vezes voce quer que seu nome seja repetido: ")))
#for i in range(cont):
#    print(nome)

#################################################################################################

#soma = 0
#for cont in range(1,101):
#    soma = soma + cont
#print("Soma de 1 a 100 é: ",soma)

#################################################################################################

#soma = 0
#somaimp = 0
#for i in range(101):
#    if i %2 == 0:
#        soma = soma + i
#
#    else:
#        somaimp = somaimp + i
#
#print("A soma dos numeros pares de 1 a 100 é:",soma)
#print("A soma dos numeros impares de 1 a 100 é:",somaimp)

#################################################################################################

#numini = int(input("Digite o numero inicial: "))
#numfim = int(input("Digite o numero final: "))
#div = int(input("Digite o numero para ser divisivel"))
#
#if numini <= numfim:
#    for i in range(numini,numfim+1):
#        if i%div == 0:
#            print(i,end=" ")
#else:
#    print("Numero Invalido")

#################################################################################################

#cont = 1
#while cont <=100:
#    print(cont, end=" ")
#    cont += 1
#print("\n")
#for cont in range(100,0,-1):
#    print(cont, end=" ")

#################################################################################################

import random
random.randint(0,10)
while True:
    mult = float
    ale1=random.randint(0,10)
    ale2=random.randint(0,10)
    mult = ale1 * ale2
    print(f"{ale1} * {ale2} = {mult}")
    resul=input(f"Qual o resultado da multiplicação de {ale1} X {ale2}?")
    if resul == mult:
        print("Acertou")
    else:
        print("Errou")
    
    break