arq = open('atp_matches_2017.csv','r')
d = {}

for linha in arq:
    nome = linha.split(',')[10]
    surface = linha.split(',')[2]

    if nome not in d:
        d[nome] = [1,1,1]

    else:
        if surface == 'Hard':
            d[nome][0] += 1

        if surface == 'Grass':
            d[nome][1] += 1

        if surface == 'Clay':
            d[nome][2] += 1

    hard = max(d, key = lambda k: d[k][0])
    grass = max(d, key = lambda k: d[k][1])
    clay = max(d, key = lambda k: d[k][2])

arq.close()



print('Jogadores com o maior número de vitórias em 2017:')
print('Cimento:{} com um total de {} vitórias.' .format(hard, d[hard][0]))
print('Grama: {} com um total de {} vitórias.' .format(grass, d[grass][1]))
print('Saibro: {} com um total de {} vitórias.' .format(clay, d[clay][2]))