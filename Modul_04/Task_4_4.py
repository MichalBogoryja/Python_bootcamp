import logging
import time
import math
from functools import reduce

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

number = ['Pierwszą', 'Drugą', 'Kolejną']


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


def report_printing(numbers, executed_operation, outcome):
    report = f'''
    Podałeś liczby: {numbers}
    Wynik ich {executed_operation} to: {outcome}
    '''
    return report


possible_operations = {
    '+': [adding, 'dodawania'],
    '-': (subtracting, 'odejmowania'),
    '*': (multiplying, 'mnożenia'),
    '/': (dividing, 'dzielenia')
}


def operation_choice():
    while True:
        operation_type = input(f'Podaj typ działania jaki chcesz wykonać '
                               f'(dostepne: {list(possible_operations.keys())})')
        if operation_type not in possible_operations:
            logging.warning("Podałeś nieprawidłowe działanie!")
            time.sleep(.1)
        else:
            break

    return operation_type


def gathering_number(operation):
    values = []
    while True:
        i = len(values)
        if i >= 2:
            if operation == '/':
                break
            if input(f'Czy chesz podać więcej liczb [T]?').capitalize() != 'T':
                break
            i = 2

        new_value = input(f'Podaj {number[i]} liczbę')
        if new_value.replace('.', '').isnumeric():
            values.append(float(new_value))
        else:
            logging.warning("Nie podałeś liczby!")
            time.sleep(.1)

    return values


def main():
    operation_type = operation_choice()
    in_values = (gathering_number(operation_type))
    result = resulting(operation_type, in_values)
    print(report_printing(in_values, possible_operations[operation_type][1], result))


if __name__ == "__main__":
    main()
