var = True
cont = 0
lista = []
while var:
    num = int(input("num: "))
    cont += 1
    lista.append(num) 
    if cont == 3:
        var = False

result = lista[0] + lista[1] + lista[2]
print(result)


