entrada= input("digite a sequencia de dna: ").upper()

#nucleotidios 
A=0
C=0
T=0
G=0
charInvalidos=0

#varrendo o input (sequencia de DNA)
for i in entrada:
	if i== "A":
		A+=1
	elif i== "C":
		C+=1
	elif i== "T":
		T+=1
	elif i== "G":
		G+=1
	else:
		charInvalidos+=1

total= A+C+T+G+charInvalidos

#porcentagem de nucleotidios 
porcA= A/total*100
porcC= C/total*100
porcT= T/total*100
porcG= G/total*100
porcInvalidos= charInvalidos/total*100

print("A:{:.1f}% C:{:.1f}% T:{:.1f}%  G:{:.1f}% INVA:{:.1f}%".format(porcA,porcC,porcT,porcG,porcInvalidos))










