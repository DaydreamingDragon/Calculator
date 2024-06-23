import math

# Get input for first number
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
            print("Please enter a valid decimal number, pi, e, or tau!")
            quit()

# Get input for calculator function
print("Exponent raises the first number to the power of the second number and mod returns the remainder of the first number divided by the second number.")
function = input("Enter function: add, subtract, multiply, divide, exponent, or mod: ")
if function != "add" and function != "subtract" and function != "multiply" and function != "divide" and function != "exponent" and function != "mod":
    print("Please enter a function listed above!")
    quit()

# Get input for second number
input2 = input("Enter second number: (type pi for pi, tau for tau, or e for euler's number): ")
if input2 == "pi":
    n2 = math.pi
elif input2 == "e":
    n2 = math.e
elif input2 == "tau":
    n2 = math.tau
else:
    try:
        n2 = int(input2)
    except ValueError:
        try:
            n2 = float(input2)
        except ValueError:
            print("Please enter a valid decimal number, pi, e, or tau!")
            quit()

# Perform function
if function == "add":
    result = n1 + n2
elif function == "subtract":
    result = n1 - n2
elif function == "multiply":
    result = n1 * n2
elif function == "divide":
    result = n1 / n2
elif function == "exponent":
    result = n1 ** n2
elif function == "mod":
    result = n1 % n2
print(f"{result}")