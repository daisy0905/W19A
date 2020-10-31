import addition
import subtraction
import multiplication
import division

# class Error(Exception):
#     pass

# class CalculatorInputError(Error):
#     pass

print("Welcome to the simple calculator, please select from the following options: ")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

userSelection = input("Please enter your selection: ")
if userSelection in ("1", "2", "3", "4"):
    print("Please enter your first number: ")
    while(True):
        try: 
            numberOne = int(input())
            break
        except ValueError:
            print("You have input invalid Character.")

    # numberOne = int(input())
    # while(True):
    #     try: 
    #         if numberOne is not int:
    #             raise CalculatorInputError
    #         break
    #     except CalculatorInputError:
    #         print("You have input invalid Character.")

    print("Please enter your second number: ")
    while(True):
        try: 
            numberTwo = int(input())
            break
        except ValueError:
            print("You have input invalid Character.")
    if userSelection == "1":
        print("Your result: " + str(addition.add(numberOne, numberTwo)))
    elif userSelection == "2":
        print("Your result: " + str(subtraction.subtract(numberOne, numberTwo)))
    elif userSelection == "3":
        print("Your result: " + str(multiplication.multiply(numberOne, numberTwo)))
    elif userSelection == "4":
        print("Your result: " + str(division.divide(numberOne, numberTwo)))

userSelection = input("Please enter your selection: ")
if userSelection in ("1", "2", "3", "4"):
    print("Enter a list of numbers, SEPARATED by WHITE SPACE: ")
    while(True):
        try:
            myList = input()
            myList = myList.split()
            numbers = []
            for number in myList:
                numbers.append(int(number))
            break
        except ValueError:
            print("You have input invalid Character.")
    if userSelection == "1":
        print("Your result: " + str(addition.addList(numbers)))
    elif userSelection == "2":
        print("Your result: " + str(subtraction.subtractList(numbers)))
    elif userSelection == "3":
        print("Your result: " + str(multiplication.multiplyList(numbers)))
    elif userSelection == "4":
        print("Your result: " + str(division.divideList(numbers)))
    
