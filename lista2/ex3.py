print ("olá!")
nome= input("qual é o seu nome?")
print ("certo" , nome , "vamos prosseguir! :)")
idade= input("quantos anos tens?")
altura= float(input("qual sua altura?"))
peso= float(input("quanto você pesa?"))
imc= float(peso/altura**2) 
print ("seu imc é: {}".format(imc))
if imc>25:
    print("voce esta acima do peso, va malha, va")
else:
    print("ta no shape ein!")    

