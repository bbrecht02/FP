import time
x= int(input("Quanto voce deseja sacar?"))
c100= x//100
resto=x%100
c50= resto//50
resto= resto%50
c20= resto//20
resto= resto%20
c10= resto//10
resto= resto%10
c5= resto//5
resto= resto%5
c1= resto//1
print("contando.....")
time.sleep(3)
print("{} notas de 100".format(c100))
print("{} notas de 50".format(c50))
print("{} notas de 20".format(c20))
print("{} notas de 10".format(c10))
print("{} notas de 5".format(c5))
print("{} notas de 1".format(c1))
