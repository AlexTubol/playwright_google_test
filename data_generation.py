import random
import operator

list_arithmetic_operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def generating_test_data() -> list:
    arithmetic_operation = []

    for oper in list_arithmetic_operators:
        numbers, data = [], []
        for x in range(2):
            numbers.append(random.randrange(1, 100, 1))
        expression = f"{numbers[0]} {oper} {numbers[1]} ="
        data.append(expression)
        result = str(list_arithmetic_operators[oper](numbers[0], numbers[1]))

        if oper == '/':
            if len(result.split(".")[1]) > 11:
                result = f'{result.split(".")[0]}.{result.split(".")[1][:11]}'
        data.append(result)
        arithmetic_operation.append(data)
    return arithmetic_operation


print(generating_test_data())
