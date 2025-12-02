#valorsalario=float(input("Qual o valor do salario?"))
#reajustesalario=float(input("Qual a porcentagem de reajuste?"))
#valorfinal=valorsalario*(reajustesalario/100)
#print("Valor do salario final = R$", valorfinal+valorsalario)

####################################################################################################################################################################################################

#vlitro=float(input("Qual o preço do combustivel?"))
#dveiculo=float(input("Qual o desempenho do seu veiculo?"))
#dcidades=float(input("Qual a distancia entre as cidades?"))
#lgastos=(dcidades/dveiculo)
#final=lgastos*vlitro
#print("Para viajar",dcidades,"kilometros irá gastar",lgastos,"litros e custará R$",final)

####################################################################################################################################################################################################

#vtotais=int(input("Numero totais de votos:"))
#vvalido=int(input("Numero de votos validos:"))
#vbranco=int(input("Numero de votos brancos:"))
#vnulo=int(input("Numero de votos nulos:"))
#pv=float((vvalido/vtotais)*100)
#pb=float((vbranco/vtotais)*100)
#pn=float((vnulo/vtotais)*100)
#print(f"Do total de {vtotais:.0f} eleitores {pv:.2f}% foram votos validos {pb:.2f}% foram de votos nulos e {pn:.2f}% foram de votos nulos")

####################################################################################################################################################################################################

#a=float(input("Valor de A = "))
#b=float(input("Valor de B = "))
#if a>b:
#    print("A maior que B")
#else:
#    if a<b:    
#        print("B maior que A")
#    else:
#        print("A igual a B")

####################################################################################################################################################################################################

#letra = input("Qual a letra: ")
#if letra == "A" or letra == "a":
#    print("1º posição")
#else:
#    if letra == "B" or letra == "b":
#        print("2º posição")
#    else:
#        if letra == "C" or letra == "c":
#            print("3º posição")
#        else:
#            if letra == "D" or letra == "d":
#                print("4º posição")
#            else:
#                if letra == "E" or letra == "e":
#                    print("5º posição")
#                else:
#                    if letra == "F" or letra == "f":
#                        print("6º posição")
#                    else:
#                        if letra == "G" or letra == "g":
#                            print("7º posição")
#                        else:
#                            if letra == "H" or letra == "h":
#                                print("8º posição")
#                            else:
#                                if letra == "I" or letra == "i":
#                                    print("9º posição")
#                                else:
#                                    if letra == "J" or letra == "j":
#                                        print("10º posição")
#                                    else:
#                                        if letra == "K" or letra == "k":
#                                            print("11º posição")
#                                        else:
#                                            if letra == "L" or letra == "l":
#                                                print("12º posição")
#                                            else:
#                                                if letra == "M" or letra == "m":
#                                                    print("13º posição")
#                                                else:
#                                                    if letra == "N" or letra == "n":
#                                                        print("14º posição")
#                                                    else:
#                                                        if letra == "O" or letra == "o":
#                                                            print("15º posição")
#                                                        else:
#                                                            if letra == "P" or letra == "p":
#                                                                print("16º posição")
#                                                            else:
#                                                                if letra == "Q" or letra == "q":
#                                                                    print("17º posição")
#                                                                else:
#                                                                    if letra == "R" or letra == "r":
#                                                                        print("18º posição")
#                                                                    else:
#                                                                        if letra == "S" or letra == "s":
#                                                                            print("19º posição")
#                                                                        else:
#                                                                            if letra == "T" or letra == "t":
#                                                                                print("20º posição")
#                                                                            else:
#                                                                                if letra == "U" or letra == "u":
#                                                                                    print("21º posição")
#                                                                                else:
#                                                                                    if letra == "V" or letra == "v":
#                                                                                        print("22º posição")
#                                                                                    else:
#                                                                                        if letra == "W" or letra == "w":
#                                                                                            print("23º posição")
#                                                                                        else:
#                                                                                            if letra == "X" or letra == "x":
#                                                                                                print("24º posição")
#                                                                                            else:
#                                                                                                if letra == "Y" or letra == "y":
#                                                                                                    print("25º posição")
#                                                                                                else:
#                                                                                                    if letra == "Z" or letra == "z":
#                                                                                                        print("26º posição")
#                                                                                                    else:
#                                                                                                        print("Digite novamente uma LETRA")

####################################################################################################################################################################################################

#capElev=int(input("Qual a capacidade maxima do elevador?: "))
#p1=float(input("Peso pessoa 1: "))
#p2=float(input("Peso pessoa 2: "))
#p3=float(input("Peso pessoa 3: "))
#p4=float(input("Peso pessoa 4: "))
#p5=float(input("Peso pessoa 5: "))
#if capElev < (p1+p2+p3+p4+p5):
#    print("Soma das 5 pessoa excede a carga maxima")
#else:
#    print("Elevador liberado")

####################################################################################################################################################################################################

x=float(input("Digite 1 se quiser calcular o volume de uma lata de oleo, ou, 2 se quiser calcular o volume de uma caixa de papelão: "))
if x==1:
    altura=float(input("Digite a altura da lata: "))
    raio=float(input("Digite o raio da lata: "))
    volumeL=3.14159*(raio**2)*altura
    print("O volume da lata é: ",volumeL,"L³")
else:
    if x==2:
        altura=float(input("Digite a altura da caixa: "))
        largura=float(input("Digite a largura da caixa: "))
        compri=float(input("Digite o comprimento da caixa: "))
        volumeC=altura*largura*compri
        print("O volume da caixa é: ",volumeC,"M³")
    else:
        print("Informação errada")

####################################################################################################################################################################################################

