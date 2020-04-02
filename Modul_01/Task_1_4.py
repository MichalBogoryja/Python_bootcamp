rows_1 = 10
columns_1 = 10
star = "* "

rows_2 = 8

rows_3 = 6

image_1 = ""
for row in range(rows_1):
    if row % 2 == 0 and row != 0:
        image_1 += " "
    image_1 += f"{star*columns_1}\n"

image_2 = "\n\n"
for row in range(rows_2):
    if row % 2 == 0:
        for i in range(row+2):
            image_2 += "*"
    else:
        for i in range(row+1):
            image_2 += "*"
    image_2 += "\n"

image_3 = "\n\n"
for row in range(rows_3, 0, -1):
    for i in range(row):
        image_3 += "*"
    image_3 += "\n"

print(image_1)
print(image_2)
print(image_3)