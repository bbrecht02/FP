entrada = str(input("digite a sequencia de DNA: ")).upper()
A = 0
C = 0
T = 0 
G = 0
Charinvi = 0
for merda in entrada:
	if merda == "A":
		A+= 1
	elif merda== "C":
		C+=1
	elif merda== "T":
		T+=1
	elif merda== "G":
		G+=1
	else:
		Charinvi+=1

total = A + C + T + G + Charinvi 
porcA = A/total*100
porcC = C/total*100
porcT = T/total*100
porcG = G/total*100
Charinvi = Charinvi/total*100


print("A: {:.1f} C: {:.1f} T: {:.1f} G: {:.1f}".format(porcA,porcC,porcT,porcG))












