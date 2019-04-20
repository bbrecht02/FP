#uber da galera
print("valor do aluguel do carro")
km1= float(input("insira a quilometragem rodada:"))
d1= float(input("agora insira a quantidade de dias a qual ficou com o carro:"))
km= 0.15 
d= 60
vtotal= float(d*d1)+(km1*km)
print("O valor total a pagar é: R${}".format(vtotal))