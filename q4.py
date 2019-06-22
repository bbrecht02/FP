def mutate(palavra):

    words= []
    palavra= palavra.lower()

    letras= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for i in range(len(palavra)+1):
        for l in letras:
                   words.append(palavra[:i] + l + palavra[i:])
                   
    for i in range(len(palavra)):
        words.append(palavra[:i]+palavra[i+1:])

    for i in range(len(palavra)):
        words.append(palavra[:i]+palavra[i+1:])


    print(words)


mutate("bennyson")

        
                   
