num= int(input("Digite um numero:"))
soma= 0
cont= 0
produto= 1
maior= num
menor= num
while num >=0:
	soma= soma + num
	cont= cont + 1
	produto= produto * num
	if num > maior:
		maior = num
	if num < menor:
		menor = num
	num= int(input("Digite um numero:"))

if cont > 0:
	media = soma/cont
else:
    media = 0
    produto = None	
    maior= 0
    menor= 0

media = soma/cont
print ("Soma:",soma)
print("Media:",media)
print("produto:",produto)
print("Menor Numero:",menor)
print("Maior Numero:",maior)
