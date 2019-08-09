def url_valida(x):


    posi1 = x.find("http")
    posi2 = x.find(":")
    posi3 = x.find("//")
    posi4 = x.count(".")


    if posi1 == 0 or posi == "http":
        x = True
        if posi2 == 4 or posi2 == ":":
            x = True
            if posi3 == 5 or posi3 == "//":
                x = True
                if posi4 >= 1 and posi4 <=3:
                    x = True
                else:
                    x = False
            else:
                x = False
        else:
            x = False
    else:
        x = False

    print(x)
    if x == True:
        print("Url valida")
    else:
        print("Url invalida")


url_valida("http://www.youtube.com.br")



