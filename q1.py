def serie_fibonacci(n):
    fibonacci= [0, 1]
    if n > 2:
        for i in range(2,n):
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
            print("fibonacci")
    else:
        print("entrada invalida")


serie_fibonacci(5)
                             
                             
