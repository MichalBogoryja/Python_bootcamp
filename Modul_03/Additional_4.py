dice = {}
available = set()
dice[2] = {(1,1)}
dice[3] = {(2,1),(1,2)}

for i in range(1,7):
    for x in range(1,7):
        available |= {(i,x)}

for i in range(2,13):
    dice[i] = set()
    for combination in available:
        if combination[0] + combination[1] == i:
            dice[i] |= {combination}