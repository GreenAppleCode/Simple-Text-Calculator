
def calculator():
    def add(a, b):
        print(a + b)

    def subtract(a, b):
        print(a - b)

    def multiply(a, b):
        print(a * b)

    def divide(a, b):
        print(a / b)

    operator = input("What operator would you like to use?(+, -, *, /): ")

    if operator == "+":
        num1 = input("What is the first number?: ")
        num1 = int(num1)
        num2 = input("What is the second number?: ")
        num2 = int(num2)
        add(num1, num2)

    elif operator == "-":
        num1 = input("What is the first number?: ")
        num1 = int(num1)
        num2 = input("What is the second number?: ")
        num2 = int(num2)
        subtract(num1, num2)

    elif operator == "*":
        num1 = input("What is the first number?: ")
        num1 = int(num1)
        num2 = input("What is the second number?: ")
        num2 = int(num2)
        multiply(num1, num2)

    elif operator == "/":
        num1 = input("What is the first number?: ")
        num1 = int(num1)
        num2 = input("What is the second number?: ")
        num2 = int(num2)
        divide(num1, num2)

    else:
        print("Invalid Syntax, Closing Program...")
        exit()
    yorn = input("Do you want to try again?(y/n): ")
    if yorn == "y":
        calculator()
    elif yorn == "Y":
        calculator()
    elif yorn == "n":
        print("Thanks for trying out my calculator!")
        exit()
    elif yorn == "N":
        print("Thanks for trying out my calculator!")
        exit()
    else:
        print("Invalid Syntax, Closing Program...")
        exit()
calculator()