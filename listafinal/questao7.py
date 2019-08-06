a= input("digite algo: ")
numero= 0
letra= 0
for i in a:
	if i.isalpha():
		letra+= 1
	elif i.isdigit():
		numero+= 1
	elif i.isspace():
		letra+= 1
	

print(numero)
print(letra)
