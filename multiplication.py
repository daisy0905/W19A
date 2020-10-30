def multiply(arg1, arg2):
    result = int(arg1) * int(arg2)
    return result

numbers = []
def multiplyList(numbers):
    result = 1
    for number in numbers:
        result = result * int(number)
    return result