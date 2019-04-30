def linhas():
    print('='*75)
while True:
    try:
        num = float(input("Digite um numero inteiro:\n\n"))
        linhas()
        break
    except ValueError:
        print ("Por acaso você é leigo?")
        linhas()

def binario(num):
    final ="0,"
    res = 999
    while res != 1:
        res = num * 2
        if res > 1:
            num = res-1
        else:
            num = res
        final = final + str(int(res))
    print("Convertendo para BINÁRIO é igual a:\n")
    print("{:.6}".format(final))
linhas()
while True:
    print ('''Escolha uma das bases de conversão:
[1] converter para BINÁRIO    
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')

    opção = int(input("Sua opção:\n"))
    linhas()
    if opção == 1:
        if num > 0 and num <= 0.9999999999999999999999:
            binario(num)
            break        
        else:
            print ("{} convertido para BINÁRIO é igual a:\n\n{}".format(num, bin(int(num))))
            linhas()
            break
    elif opção == 2:
        print ("{} convertido para OCTAL é igual a:\n\n{}".format(num, oct(int(num))))
        linhas()
        break
    elif opção == 3:
        print ("{} convertido para HEXADECIMAL é igual a:\n\n{}".format(num, hex(int(num))))
        linhas()
        break
    else:
        print ("Opção invalida. Tente novamente")
        linhas()
