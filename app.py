import addition
import subtraction
import multiplication
import division

print("Welcome to the simple calculator, please select from the following options: ")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

userSelection = input("Please enter your selection: ")
if userSelection in ("1", "2", "3", "4"):
    input("Please enter your first number: ")
    numberOne = input()
    input("Please enter your second number: ")
    numberTwo = input()
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
    myList = input("Enter a list of numbers, SEPARATED by WHITE SPACE: ")
    myList = myList.split()
    if userSelection == "1":
        print("Your result: " + str(addition.addList(myList)))
    elif userSelection == "2":
        print("Your result: " + str(subtraction.subtractList(myList)))
    elif userSelection == "3":
        print("Your result: " + str(multiplication.multiplyList(myList)))
    elif userSelection == "4":
        print("Your result: " + str(division.divideList(myList)))

    
