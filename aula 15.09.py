#letra=input("Digite uma letra: ").upper().strip()
#if letra in "AEIOU":
#    print("Letra é uma vogal")
#elif not letra.isalpha():
#    print("Voce digitou um numero ou simbolo, digite uma letra")
#else:
#    print("Letra é consoante")

##############################################################################################################################

#n1=float(input("Digite a nota da P1: "))
#n2=float(input("Digite a nota da P2: "))
#al=int(input("Digite o numero de aulas: "))
#ft=int(input("Digite o numero de faltas: "))
#if (n1+n2)/2 >=7 and (al-ft)*100/al >= 75:
#    print("APROVADO")
#else:
#    print("REPROVADO")

##############################################################################################################################

#alt=float(input("Digite sua altura: "))
#gen=str(input("Digite seu genero, M & F: ")).upper()
#if gen == "M":
#    pesoid=(72.7*alt)-58
#    print(f"Seu peso ideal é, {pesoid:.2f}Kg")
#elif gen == "F":
#    pesoid=(62.1*alt)-44.7
#    print(f"Seu peso ideal é {pesoid:.2f}Kg")
#else:
#    print("Refaça o processo")
    
##############################################################################################################################

#ano = int(input("Digite o ano que você deseja saber se é bissexto ou não: "))
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#  print(f"O ano {ano} é um ano bissexto")
#else:
#  print(f"Não é um ano bissexto")

##############################################################################################################################

#n1=float(input("Digite um numero positivo: "))
#n2=float(input("Digite outro numero positivo: "))
#op=str(input("Digite a operação escolhida: + - / * : "))
#if op == "+" :
#    total=n1+n2
#    print(f"Resultado: {n1} + {n2} = {total:.3f}")
#elif op == "-" :
#    total=n1-n2
#    print(f"Resultado: {n1} - {n2} = {total:.3f}")
#elif op == "/" :
#    total=n1/n2
#    print(f"Resultado: {n1} / {n2} = {total:.3f}")
#elif op == "*" :
#    total=n1*n2
#    print(f"Resultado: {n1} * {n2} = {total:.3f}")
#
#else:
#    print("Digite novamente a operação")

##############################################################################################################################

#pla=input("Digite sua placa: ")
#pl = pla[-1]
#
#if pl in ['1', '2']:
#    print("Seu dia de rodizio é segunda feira")
#elif pl in ['3', '4']:
#    print("Seu dia de rodizio é terça feira")
#elif pl in ['5', '6']:
#    print("Seu dia de rodizio é quarta feira")
#elif pl in ['7', '8']:
#    print("Seu dia de rodizio é quinta feira")
#elif pl in ['9', '0']:
#    print("Seu dia de rodizio é sexta feira")
#else:
#    print("Digite novamente o final da sua placa")

##############################################################################################################################

sl = float(input("Digite o seu salario: "))
pr = float(input("Qual o valor da prestação do emprestimo: "))
if float(sl < pr * 0.20):
  print("Emprestimo não concedido")
else:
  print("Emprestimo concedido")