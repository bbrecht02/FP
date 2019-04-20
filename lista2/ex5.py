print("digite o valor da casa a qual pretendes comprar")
vcasa= int(input("valor:\n"))
salario= int(input("qual o seu salario:\n"))
anos= int(input("por quantos anos voce pretende pagar:\n"))	
mensais= int(vcasa/(anos*12))
porc= salario*30/100
if mensais<porc:
	print("voce pode comprar a casa e pagara {} reais mensais".format(mensais))
else:
	print("voce nao pode comprar a casa pois o valor de {} reais mensais nao condiz com sua renda".format(mensais))
	

