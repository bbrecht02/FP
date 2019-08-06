entrada= str(input("digite sua palavra:"))
palavra = entrada.split()
junto = " ".join(palavra)
inverso = junto[::-1]
print(f"o inverso de {junto} é {inverso}")  
if junto == inverso:
	print("palindromo")

else:
	print("nao palindromo")
