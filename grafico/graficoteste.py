import matplotlib.pyplot as plt 

x= []
y= []

data= open("/home/bennyson/Documentos/codigos/grafico.txt","r")

for line in data:
    line = line.strip()
    X, Y = line.split(',')
    x.append(X)
    y.append(Y)
    
data.close()

plt.plot(x, y)

plt.title("gráfico")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

plt.show()
