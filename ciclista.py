#code by benny
cont=0
meta=8.0
day1= float(input("digite sua quilometragem percorrida no primeiro dia:"))
if (day1>=meta):
     cont+=1	
day2= float(input("digite sua quilometragem percorrida no segundo dia:"))
if (day2>=meta):
     cont+=1
day3= float(input("digite sua quilometragem percorrida no terceiro dia:"))
if (day3>=meta):
     cont+=1
day4= float(input("digite sua quilometragem percorrida no quarto dia:"))
if (day4>=meta):
     cont+=1
day5= float(input("digite sua quilometragem percorrida no quinto dia:"))
if (day5>=meta):
     cont+=1
day6= float(input("digite sua quilometragem percorrida no sexto dia:"))
if (day6>=meta):
     cont+=1
day7= float(input("digite sua quilometragem percorrida no setimo dia:"))
if(day7>=meta):
     cont+=1
print("voce cumpriu a meta por {} dias".format(cont))
if cont>=5:
   print("Desempenho otimo")
if cont==3:
   print("Desempenho razoavel")
if cont==4:
   print("Desempenho razoavel")         
if cont<3:
   print("Desempenho ruim")   
#m= float(day1+day2+day3+day4+day5+day6+day7) 
#otimo 5 ou+
# razoavel 3 ou 4
# ruim menos de 3