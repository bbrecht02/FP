d= {1:2, 3:4, 5:6}
def inva(dicionario):
	invertido= {}
	for i in dicionario:
		invertido[dicionario[i]] = []
	for i in dicionario:
		invertido[dicionario[i]].append(i)
	print(invertido)


inva(d)
