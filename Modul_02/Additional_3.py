num = 30
fibonacci = []

for i in range(num):
    if i < 2:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])

print(fibonacci)