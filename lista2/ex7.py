print("digite um ano:")
ano= int(input("ano:"))
if ano%400==0 or ano%4==0:
	print("é bissexto!")
elif ano%100==0:
	print("não é bissexto")
else:
	print("não é bissexto!")		