from random import randint

a= []
maior= 0
menor= 50

for x in range(50):
	a.append(randint(0,50))

for x in a:
	if x > maior:
		maior= x
	elif x < menor:
		menor= x

print(f'O maior numero foi {maior} e o menor foi {menor}')
