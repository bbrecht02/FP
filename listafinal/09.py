cont= 0 
n= "101"  
m= "1101010011010"
var= True
start= 0
while var:
	#for i in m:
	a = m.find(n, start)
	if a == -1:
		var= False 
	else:
		cont += 1
		start = a+1

print(cont)