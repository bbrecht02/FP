def linhas(lalala):
	try:
		arquivo= open("lalala.txt","r")
		arquivo.close()

	except:
		return("falha ao abrir!")

	try:
		arquivo= open("lalala.txt","r")
		txt= arquivo.read()

	except:
		return("falha ao ler!")


	arquivo = open("lalala.txt","r")
	txt= arquivo.read()
	x= 0
	for i in txt:
		if i == " ":
			x+=1

	return(x)


lalala= "lalala.txt"
print(linhas(lalala))

