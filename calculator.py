import math

input1 = input("Enter first number: (type pi for pi, tau for tau, or e for euler's number): ")
if input1 == "pi":
    n1 = math.pi
elif input1 == "e":
    n1 = math.e
elif input1 == "tau":
    n1 = math.tau
else:
    try:
        n1 = int(input1)
    except ValueError:
        try:
            n1 = float(input1)
        except ValueError:
            print("Please enter a valid decimal number or pi!")
            quit()

function = input("Enter function: add, subtract, multiply, divide, exponent, mod: ")
if function != "add" and function != "subtract" and function != "multiply" and function != "divide" and function != "exponent" and function != "mod":
    print("Please enter a function listed above!")
    quit()

