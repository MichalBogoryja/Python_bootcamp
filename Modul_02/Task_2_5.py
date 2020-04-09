# Zadanie 1
limit = 10

cube = [num ** 3 for num in range(1, limit+1)]
cube_org = cube[:]
report = f"Zadnie #1\nLista szecianów: {cube}\n"

for num in cube:
    if num % 2 == 0:
        cube.remove(num)

cube_2 = [num ** 3 for num in range(1, limit+1) if num % 2 == 1]
cube_3 = list(filter(lambda x : x % 2 == 1, [num ** 3 for num in range(1,limit+1)]))
[cube_org.remove(num) for num in cube_org if num % 2 == 0]


report += f"Lista szecianów niepodzielnych przez 2 (metoda z polecenia): {cube}\n"
report += f"Lista szecianów niepodzielnych przez 2 (metoda alternatywna#1): {cube_2}\n"
report += f"Lista szecianów niepodzielnych przez 2 (metoda alternatywna#2): {cube_3}\n"
report += f"Lista szecianów niepodzielnych przez 2 (metoda alternatywna#3): {cube_org}\n\n"

# Zadanie 2
initial_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]

zeros = initial_list[1:4] + initial_list[5:10] + initial_list[-2:]
report += f"Zadnie #2\nLista zer: {zeros}\n"

not_zeros = initial_list[:1] + initial_list[4:5] + initial_list[-4:-2]
report += f"Lista nie-zer: {not_zeros}\n"

print(report)
