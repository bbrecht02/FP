def url(string):
	posi= string.find("http")
	posi2= string.find(":")
	posi3= string.find("//")
	posi4= string.count(".")



	if posi== 0 or posi== "http":
		string= True
		if posi2== 4 or posi2== ":":
			string= True
			if posi3== 5 or posi3== "//":
				string= True
				if posi4>= 1 and posi4 <=3:
					string= True
				else:
					string= False
					print("url invalida")
			else:
				string= False
				print("url invalida")
		else:
			string= False
			print("url invalida")
	else:
		string= False
		print("url invalida")

	if string== True:
		print("url valida")

url("http://cesar.school")



