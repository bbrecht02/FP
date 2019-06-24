def serie_fibonacci(n):
    fibonacci= [0, 1]
    if n >= 2:
        for i in range(2,n):
            n= int(input("n?"))
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
            print(fibonacci)
    else:
        print("erro")


serie_fibonacci(10)
                             
                             
