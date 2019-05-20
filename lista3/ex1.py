b= 2
p= 0
n= int(input("digite um numero:"))
while abs(n - p**2) > 0.0001:
    p=(b+(n/b))/2
    b= p
    print(p**2)
    p=(b+(n/b))/2
    print(p**2)
    if abs(n - p**2) < 0.0001:
    	break
print("raiz quadrada de {} equivale a {}".format(n,p))
