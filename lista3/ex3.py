cima= float(input("diga a distancia para cima:\n"))
baixo= float(input("diga a distancia para baixo:\n"))
baixo= -baixo #eixo

esquerda= float(input("diga a distancia para a esquerda:\n")) 
direita= float(input("diga a distancia para a direita:\n"))
direita= -direita #eixo

x= (cima+baixo) #eixo x
y= (esquerda+direita) #eixo y
print("Y = {} X = {}".format(y,x))


distancia= (y**2) + (x**2)
distancia= distancia**0.5 #esqueci a funçao de raiz kkk
print("distancia = {:.3f}".format(distancia))