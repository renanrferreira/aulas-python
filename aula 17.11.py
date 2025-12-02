#M = [[1,2,3],[4,5,6]]
#print(M)

##################################################################################################################################

#M = [0] * 2
#for i in range(2):
#    M[i] = [0] * 3
#    for j in range(3):
#        M[i][j] = 1
#print(M)

##################################################################################################################################

#M = [0] * 3
#M[0] = [1,1,1]
#M[1] = [2,2,2]
#M[2] = [3,3,3]
#print(M)

##################################################################################################################################

#M = [[1,2,3],[4,5,6]]
#print(M[0][1])

##################################################################################################################################

#M = [[1,2,3],[4,5,6]]
#for i in range(0,2):
#    for j in  range(0,3):
#        print("[{:^3}]".format(M[i][j]),end="")
#    print()

##################################################################################################################################

## Adicionar elementos na matriz metodo comum
#M = [0] * 2
#for i in range(0,2):
#    M[i] = [0] * 3
#    for j in range(0,3):
#        M[i][j] = int(input("Digite o valor [{}][{}] -> ".format(i,j)))
#print(M)
#
## Adicionar elementos na matriz funcao append()
#M=[]
#for i in range(0, 2):
#    M.append([])
#    for j in range(0,3):
#        M[i] .append(int(input("Digite valor [ {} ] [ {} ] ->  ".format(i,j))))
#print(M)

##################################################################################################################################

#from random import randint
#M = []
#for i in range(0,2):
#    M.append([])
#    for j in range(0,3):
#        M[i].append(randint(1,50))
#print(M)

##################################################################################################################################

#M=[]
#soma = 0
#for i in range(0, 2):
#    M.append([])
#    for j in range(0,3):
#        M[i] .append(int(input("Digite valor [ {} ] [ {} ] ->  ".format(i,j))))
#        soma += M[i][j]
#print(M)
#print(f"A soma da matriz é: {soma}")

##################################################################################################################################

#soma=0
#from random import randint
#M = []
#for i in range(10):
#    M.append([])
#    for j in range(10):
#        M[i].append(randint(1,50))
#        soma += M[i][j]
#for a in M:
#    print(a)
#media = soma/100
#print("A soma de todos os numeros é: ",soma)
#print("A media de todos os numeros é: ",media)

##################################################################################################################################

#from random import randint
#M = []
#for i in range(10):
#    M.append([])
#    for j in range(10):
#        M[i].append(randint(5,38))
#for a in M:
#    print(a)
#for i in range(10):
#    somalinha = sum(M[i])
#    print(f"A soma da linha {i+1} é: {somalinha}")

##################################################################################################################################

#from random import randint
#M = []
#for i in range(10):
#    M.append([])
#    for j in range(10):
#        M[i].append(randint(1,50))
#for a in M:
#    print(a)
#for i in range(10):
#    #menor = min(M[i])
#    menor = 50
#    for j in range(10):
#        if M[i][j] < menor:
#            menor = M[i][j]
#    print(f"O menor numero da linha {i+1} é: {menor}")

##################################################################################################################################

from random import randint
M = []
for i in range(10):
    M.append([])
    for j in range(10):
        M[i].append(randint(1,50))
for a in M:
    print(a)
for j in range(10):
    menor = 50
    for i in range(10):
        if M[i][j] < menor:
            menor = M[i][j]
    print(f"O menor numero da coluna {j+1} é: {menor}")

##################################################################################################################################
