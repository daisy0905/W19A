def add(arg1, arg2):
    result = arg1 + arg2
    return result

numbers = []
def addList(numbers):
    result = 0
    for number in numbers:
        result += int(number)
    return result
