cont= 0 

senha= input("digite a senha que deseja verificar:\n")
mai= "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
minu= "A B C D E F G H I J K L M N O PQ R S T U V W X Y Z".split()
num= "0 1 2 3 4 5 6 7 8 9".split()
sim= "$ # @".split()

for car in senha:
	if car in mai:
		cont= 1

for car in senha:
	if car in minu:
		if cont== 1:
			cont= 2

for car in senha:
	if car in num:
		if cont== 2:
			cont= 3

for car in senha:
	if car in sim:
		if cont== 3:
			cont= 4


if len(senha) >= 6 and len(senha) <=12:							
	if cont== 4:
		cont= 5

if cont== 5:
	print (senha)

else:	
	print("senha invalida!")
