#aumento de salário
print("Bora lá ver qual vai ser teu aumento??")
s= int(input("Quanto tu ganha, bença?"))
a= int(input("Diz ai a porcentagem de aumento:"))
acash= (s*a)/100
newdeal= s+acash
print("dale! teu aumento foi de {} conto\n e R${} é teu novo salário".format(acash,newdeal))
