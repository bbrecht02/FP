t= 0
a= "a b c d e f g h i j k l m n o p q r s t u v w x y z"
entrada= input("digite a entrada:")
i=0
dois= str()

while i != len(entrada):
	if entrada[i] != (" "):
		dois+= entrada[1]
	i += 1
saida= str()

if entrada[:3] != ("ROT"):
	print("erro")

elif entrada[3].isalnum() == False:
	print("erro")

elif entrada[4] != (" ") and entrada[4].isalnum() == False:
	print("erro")

elif entrada[4]== (" ") and  entrada[4].isalnum() == False:
	print("erro")

elif entrada[5]== (" ") and  entrada[5].isalnum() == False:
	print("erro")

else:
	n= str()
	n= n + entrada[4]
	t = len(entrada)
	i= 5
	if entrada[4] != (" "):
		n= n+ entrada[4]
		i= 6
	n= int(n)
	
while i != t:
	if entrada[i] != (" "):
		localizacao= a.find(entrada[i].lower())
		if localizacao + n > 25:
			saida= saida + a[localizacao + n -26]
		else:
			saida = saida + a[localizacao + n]
	else:
		saida= saida + (" ")
		i+= 1
print(saida)				