entrada = str(input("digite algo:"))
letra = 0  
num = 0
for x in entrada:
	if x.isdigit():
		num += 1
	elif x.isalpha():
		letra+= 1 
	elif x.isspace():
		 letra+= 1

print(f"Letra:{letra}\nDigitos{num}")


