numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0
lowest = 0
highest = 0

for i, number in enumerate(numbers):
    if not number % 5:
        number += 1
    number = round(number, -1)
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number
    numbers[i] = number

for num in numbers:
    if num == lowest:
        numbers.remove(num)
        break

for num in numbers:
    if num == highest:
        numbers.remove(num)
        break

mean_number = sum(numbers) / len(numbers)