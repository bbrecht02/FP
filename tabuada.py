num= int(input("digite um numero:\n"))
i= 0
cont= 1
while i==0:
  print("="*8)
  print("{}x{}={}".format(num,cont,num*cont))
  cont= cont+1
  if cont==11:
    break
print("="*8)