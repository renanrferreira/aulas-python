#l1=float(input("Escreva o lado 1: "))
#l2=float(input("Escreva o lado 2: "))
#l3=float(input("Escreva o lado 3: "))
#if l1>l2+l3 or l2>l1+l3 or l3>l1+l2:
#    print("Valores nao condizem com um triangulo")
#elif l1==l2==l3:
#    print("Triangulo é equilatero!")
#elif l1!=l2!=l3:
#    print("Triangulo é escaleno!")
#else:
#    print("Triangulo é isosceles!")

####################################################################################################################################################################################################

#n1=int(input("Digite o primeiro numero: "))
#n2=int(input("Digite o segundo numero: "))
#n3=int(input("Digite o terceiro numero: "))
#if n1%2==0:
#    print("O primeiro numero:",n1,"é par")
#else:
#    print("O primeiro numero:",n1,"é impar")
#if n2%2==0:
#    print("O segundo numero:",n2,"é par")
#else:
#    print("O segundo numero:",n2,"é impar")
#if n3%2==0:
#    print("O terceiro numero:",n3,"é par")
#else:
#    print("O terceiro numero:",n3,"é impar")

####################################################################################################################################################################################################

##A, B, C, D = [int(input(f"Digite a variavel {x}: ")) for x in "ABCD"]
#A=int(input("Digite a variavel A: "))
#B=int(input("Digite a variavel B: "))
#C=int(input("Digite a variavel C: "))
#D=int(input("Digite a variavel D: "))
#if B>C and D>A and C+D>A+B and C>0 and D>0 and A%2==0:
#    print("Valores aceitos")
#else:
#    print("Valores nao aceitos")

####################################################################################################################################################################################################

#a1=int (input("Digite o valor do primeiro ângulo: "))
#a2=int (input("Digite o valor do segundo ângulo: "))
#a3=int (input("Digite o valor do terceiro ângulo: "))
#if a1+a2+a3!=180:
#  print("Os ângulos não formam um triângulo")
#elif a1<90 and a2<90 and a3<90:
#  print("Os ângulos formam um triângulo acutângulo")
#elif a1>90 or a2>90 or a3>90:
#  print("Os ângulos formam um triângulo obtusângulo")
#else:
#  print("Os ângulos formam um triângulo retângulo")

####################################################################################################################################################################################################

#id=int(input("Digite a idade do nadador: "))
#if id>=5 and id<=7:
#    print("Nadador se classica como Infantil A")
#elif id>=8 and id<=11:
#    print("Nadador se classica como Infantil B")
#elif id>=12 and id<=13:
#    print("Nadador se classifica como Juvenil A")
#elif id>=14 and id<=17:
#    print("Nadador classifica como Juvenil B")
#elif id>=18 and id<90:
#    print("Nadador se classifica como Adulto")
#elif id>=90:
#    print("Vai descansar meu filho")
#else:
#    print("Nadador nao pode ser classificado devido a idade")

####################################################################################################################################################################################################

sa = int (input("Digite o valor que você deseja sacar (somente multiplos de 10): "))

if sa % 10 != 0:
  print("Valor incorreto")
else:
  valor_restante = sa
  if valor_restante // 100:
    print(f"Você receberá {valor_restante // 100} notas de 100")
    valor_restante %= 100
  if valor_restante // 50:
    print(f"Você receberá {valor_restante // 50} notas de 50")
    valor_restante %= 50
  if valor_restante // 20:
    print(f"Você receberá {valor_restante // 20} notas de 20")
    valor_restante %= 20
  if valor_restante // 10:
    print(f"Você receberá {valor_restante // 10} notas de 10")