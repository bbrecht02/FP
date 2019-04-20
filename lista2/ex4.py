print("digite os lados do triangulo:")
l1= input("lado 1:")
l2= input("lado 2:")
l3= input("lado 3:")

if (l1+l2>l3) or (l1+l3>l2) or (l2+l3>l1):
	print("é um triangulo!")
elif (l1+l2<l3) or (l1+l3<l2) or (l2+l3<l1):
    print("não é um triangulo!")

if l1==l2 and l2==l3:
    print("é um triangulo equilatero")
elif l1==l2 or l1==l3 or l2==l3:
    print("é um triangulo isoceles")
if l1!=l2 and l1!=l3 and l2!=l3:
    print("é um triangulo escaleno")


    