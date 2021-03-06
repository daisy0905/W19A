def divide(arg1, arg2):
    try:
        result = arg1 / arg2
        return result
    except CalculatorInputError:
        print("You have entered an invalid character, please try again.")
    except ZeroDivisionError: 
        print("Sorry, you can't divide by 0!")
    finally:
        print("We have made it out alive!")

def divideList(numbers):
    result = int(numbers[0])
    for number in numbers[1:]:
        result = result / number
    return result