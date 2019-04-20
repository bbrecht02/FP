cont=0
v1= input("telefonou para a vitima?")
if (v1=="sim"):
     cont+=1	
v2= input("esteve no local do crime?")
if (v2=="sim"):
     cont+=1
v3= input("mora perto da vitima?")
if (v3=="sim"):
     cont+=1
v4= input("devia money para a vitima?")
if (v4=="sim"):
     cont+=1
v5= input("já trabalhou com a vitima?")
if (v5=="sim"):
     cont+=1  
if cont==2:
    print("suspeita")
if cont==3:
    print("cumplice")
if cont== 4:
    print("cumplice")
if cont==5:
    print("assassino")
if cont<=1:
    print("inocente")                


