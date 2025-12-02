#L = []
#print(L)

#L = [0]*5
#print(L)

#L = [0,0,0,0,0]
#print(L)

#L = [1,2,3,4,5]
#print(L[4]) #parte de 0 (primeira posicao do vetor), o numero entre [] é a posiçao que sera exibida

#L = ['a','b']
#print(L)

#L = list()
#print(L)

#num = 'se leu e gay'
#L = list(num)
#print(L)

#L = [1,2,3,4,5]
#print(len(L)) #descreve quantas posiçoes o vetor tem

############################################################################################################################################

#L = [1,2,3,4,5]
#x = 0
#while x < len(L):
#    print(L[x],end=" ")
#    x += 1

###########################################################################################################################################

#L = [9,8,7,6,5]
#for i in range(5):
#    print(L[i],end=" ")

###########################################################################################################################################

#L = [1,2,3,4,5,6]
#for item in L:
#    print(item, end=" ")

###########################################################################################################################################

#L = [0]*10
#print(L)
#for i in range(10):
#    L[i] = int(input("{}º valor -> ".format(i+1)))
#print(L)

###########################################################################################################################################

#L = []
#print(L)
#for i in range(10):
#    valor = int(input("{}º valor -> ".format(i+1)))
#    L.append(valor)
#print(L)

###########################################################################################################################################

#L = []
#print(L)
#for i in range(10):
#    L.insert (i,int(input("{}º valor -> ".format(i+1))))
#print(L)

###########################################################################################################################################

#from random import randint
#L = []
#for i in range(5):
#    L.append(randint(1,50))
#print(L)

###########################################################################################################################################

#from random import randint
#L = []
#for i in range(10):
#    L.append(randint(1,50))
#print(f"Os números gerados foram: {L}")
#tpar = 0
#timp = 0
#
#for numero in L:
#    if  numero % 2 == 0:
#        tpar += 1
#    else:
#        timp += 1
#
#print(f"Total de números pares: {tpar}")
#print(f"Total de números ímpares: {timp}")
#print(f"Total de números: {tpar + timp}")
                        
###########################################################################################################################################

#from random import randint
#
#L = []
#for i in range(20):
#  L.append(randint(1, 50))
#print(f"Os números gerados foram: {L}")
#
#par = []
#for numero in L:
#  if numero % 2 == 0:
#    par.append(numero)
#
#print(f"Os números pares encontrados foram: {par}")
#
#if len(par) > 0:
#  tpar = sum(par)
#  med = tpar / len(par) 
#  print(f"A média dos números pares é {med}")
#else:
#  print("Nenhum número par foi encontrado na lista.")

###########################################################################################################################################

#from random import randint
#L = []
#for i in range(20):
#    L.append(randint(1,50))
#print(f"Os números gerados foram: {L}")
#mu5 = []
#for numero in L:
#  if numero % 5 == 0:
#    mu5.append(numero)
#print(f"Os numeros multiplos de 5 são: {mu5}")

###########################################################################################################################################

#from random import randint
#L = []
#for i in range(20):
#    L.append(randint(1,50))
#print(f"Os números gerados foram: {L}")
#mup=int(input("Digite o numero a ser verificado: "))
#mu = []
#for num in L:
#    if num %mup == 0:
#        mu.append(num)
#print(f"Os numeros multiplos de {mup} sao: {mu}")

###########################################################################################################################################

from random import randint
L = []
for i in range(10):
    L.append(randint(1,50))
esc=int(input("Escolha entre 1(Ordenar em crescente) ou 2(Ordenar em decrescente): "))
print(f"Os numeros Aleatorios são: {L}")
if esc==1:
    for i in range(10):
        print(L[i],end=' ')
    #L.sort()
    #print(f"Os numeros aleatorios na ordem convecional sao: {L}")
elif esc ==2:
    for i in range(9,-1,-1):
        print(L[i],end=' ')
else:
    print("Opção invalida")
    #L.sort(reverse=True)
    #print(f"Os numeros aleatorios na ordem inversa sao: {L}")

###########################################################################################################################################