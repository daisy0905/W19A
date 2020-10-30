def subtract(arg1, arg2):
    result = int(arg1) - int(arg2)
    return result

numbers = []
def subtractList(numbers):
    result = int(numbers[0])
    for number in numbers[1:]:
        result -= int(number)
    return result