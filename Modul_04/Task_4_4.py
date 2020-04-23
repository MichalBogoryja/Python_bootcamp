import logging
import time
import math
from functools import reduce

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def adding(numbers):
    result = sum(numbers)
    return result


def dividing(numbers):
    result = reduce(lambda x, y: x / y, numbers)
    return result


def multiplying(numbers):
    result = math.prod(numbers)
    return result


def subtracting(numbers):
    result = reduce(lambda x, y: x - y, numbers)
    return result


def resulting(i, numbers):
    func = possible_operations.get(i)[0]
    return func(numbers)


in_values = []
possible_operations = {
    '+': [adding, 'dodawania'],
    '-': (subtracting, 'odejmowania'),
    '*': (multiplying, 'mnożenia'),
    '/': (dividing, 'dzielenia')
}
number = ['Pierwszą', 'Drugą', 'Kolejną']

while True:
    operation_type = input(f'Podaj typ działania jaki chcesz wykonać (dostepne: {list(possible_operations.keys())})')
    if operation_type not in possible_operations:
        logging.warning("Podałeś nieprawidłowe działanie!")
        time.sleep(.1)
    else:
        break

while True:
    i = len(in_values)
    if i >= 2:
        if operation_type == '/':
            break
        if input(f'Czy chesz podać więcej liczb [T]?').capitalize() != 'T':
            break
        i = 2

    new_value = input(f'Podaj {number[i]} liczbę')
    if new_value.replace('.', '').isnumeric():
        in_values.append(float(new_value))
    else:
        logging.warning("Nie podałeś liczby!")
        time.sleep(.1)

result = resulting(operation_type, in_values)

report = f'''
Podałeś liczby: {in_values}
Wynik ich {possible_operations[operation_type][1]} to: {result}
'''
print(report)
