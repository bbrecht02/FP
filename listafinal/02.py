print("Welcome to Reforma da previdencia")
sexo= str(input("Homem ou Mulher? ")).upper()
tempo= int(input("tempo de contribuicao: "))
idade= int(input("digite sua idade: "))
saida= " "
if sexo== "HOMEM":
	if idade>=65 and tempo>= 10:
		saida= "aposentavel"
	elif idade>=63 and tempo>= 15:
		saida= "aposentavel"
	else:
		saida= "nao aposentavel"

if sexo== "MULHER":
	if idade>= 63 and tempo>= 10:
		saida= "aposentavel"
	elif idade>=61 and tempo>= 15:
		saida= "aposentavel"
	else:
		saida= "nao aposentavel"

print(saida)








