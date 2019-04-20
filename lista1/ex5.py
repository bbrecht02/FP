#redução do tempo de vida 
nc= int(input("Qual o número de cigarros você fuma por dia:\n"))
anos= int(input("Há quantos anos você fuma?\n"))
cigarrospano= nc*365
legiaourbana= cigarrospano*10
total= legiaourbana*anos
dias = int(total/1440)
print("pelo meus calculos você já perdeu {} dias de vida por causa do cigarro :(".format(dias))