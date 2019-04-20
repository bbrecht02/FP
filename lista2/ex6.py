print("digite seu salario:")
salario= float(input("salario:"))
desconto= float(salario*(11/100))
if desconto>318.20:
   desconto= float(318.20)
print("o valor a ser descontado sera de: {}".format(desconto))   

