print("Ola, seja bem vindo a reforma da presidencia! rs\nVamor ver se estais apto a se aposentar:")
sexo= str(input("Homem ou Mulher? ")).lower()
idade= int(input("Qual sua idade? "))
tempo= int(input("Qual seu tempo de contribuicao? "))
result= " "
if sexo== "homem":
	if idade>=63 and tempo>=15:
		result= "aposentavel"
	elif idade>=65 and tempo>=10:
		result= "aposentavel"
	print(result)

if sexo== "mulher":
	if idade>=63 and tempo>=10:
		result= "aposentavel"
	elif idade>=61 and tempo>=15:
		result= "aposentavel"
	print(result)

else:
	print("nao aposentavel")

