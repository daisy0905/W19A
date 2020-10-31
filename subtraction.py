def subtract(arg1, arg2):
    result = arg1 - arg2
    return result

def subtractList(numbers):
    result = int(numbers[0])
    for number in numbers[1:]:
        result -= number
    return result