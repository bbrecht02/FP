num= 5
cont= 1
lista= []

while cont <= 5:
	entrada= int(input("digite {} inteiros: ".format(num)))
	cont+=1
	num-= 1
	lista.append(entrada)
	print(lista)

maior= lista[0]
menor= lista[0]


for x in lista:
	if x > maior:
		maior= x
	elif x < menor:
		menor= x

print(f"menor:{menor} maior:{maior}")
media= (lista[0]+lista[1]+lista[2]+lista[3]+lista[4])/5
print(f"media dos numeros: {media}")




