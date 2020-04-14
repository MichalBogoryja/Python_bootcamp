limit = 100
divisible = []
cube = []

for num in range(limit+1):
    if num % 5 == 0:
        divisible.append(num)
        cube.append(num**3)

result = f"""Podzielne przez 5: {divisible}
Ich 3 potęgi: {cube}
"""

print(result)