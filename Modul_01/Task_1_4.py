rows_1 = 10
columns_1 = 10

rows_2 = 8

rows_3 = 6

image_1 = f""
for row in range(rows_1):
    if row % 2 == 0 and row != 0:
        image_1 += f" "
    for column in range(columns_1):
        image_1 += f"* "
    image_1 += f"\n"

image_2 = f"\n\n"
for row in range(rows_2):
    if row % 2 == 0:
        for i in range(row+2):
            image_2 += f"*"
    else:
        for i in range(row+1):
            image_2 += f"*"
    image_2 += f"\n"

image_3 = f"\n\n"
for row in range(rows_3, 0, -1):
    for i in range(row):
        image_3 += f"*"
    image_3 += f"\n"

print(image_1)
print(image_2)
print(image_3)