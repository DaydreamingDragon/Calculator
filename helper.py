import math

def isFloat(n):
    try: 
        float(n)
    except ValueError:
        return False
    str(n)
    if "." in n:
        return float(n)
    else:
        return int(n)
    
def firstNumberInput():
      # Get input for first number
    input1 = input("Enter first number: (type pi for pi, tau for tau, or e for euler's number): ")
    if input1 == "pi":
        n1 = math.pi
    elif input1 == "e":
        n1 = math.e
    elif input1 == "tau":
        n1 = math.tau
    else:
        n1 = isFloat(input1)
        if n1 == False:
            print("Please enter a valid decimal number, pi, e, or tau!")
    return n1

def oneNumber(n1):
    # Get input for calculator function
    print("Radian converts a number from degrees to radians, degrees converts a number from raidans to degrees, ln finds the natural log of a number.")
    print("Trig functions are in radians")
    function = input("Enter function: sin, cos, tan, asin, acos, atan, sqrt, factorial, radian, degree, ln: ")

    # Perform function
    if function == "sin":
        result = math.sin(n1)
    elif function == "cos":
        result = math.cos(n1)
    elif function == "tan":
        result = math.tan(n1)
    elif function == "asin":
        result = math.asin(n1)
    elif function == "acos":
        result = math.acos(n1)
    elif function == "atan":
        result = math.atan(n1)
    elif function == "sqrt":
        result = math.sqrt(n1)
    elif function == "factorial":
        # inputted number needs to be an int for factorial
        strn1 = str(n1)
        if "." in strn1:
            print("In order to use the factorial function, you must input an integer!")
            quit()
        else:
            int(n1)
            result = math.factorial(n1)
    elif function == "radian":
        result = math.radians(n1)
    elif function == "degrees":
        result = math.degrees(n1)
    elif function == "ln":
        result = math.log(n1)
    else:
        print("Please enter a function listed above!")
        quit()
    print(f"{result}")

def twoNumbers(n1):
    # Get input for calculator function
    print("Exponent raises the first number to the power of the second number, logbase finds the log of the first number ")
    print("with the base of the second number, r and mod returns the remainder of the first number divided by the second number.")
    function = input("Enter function: add, subtract, multiply, divide, exponent, greatest common divisor, logbase, or mod: ")
    if function != "add" and function != "subtract" and function != "multiply" and function != "divide" and function != "exponent" and function != "mod" and function != "greatest common divisor" and function != "logbase":
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
       n2 = isFloat(input2)

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
    elif function == "greatest common divisor":
        strn1 = str(n1)
        strn2 = str(n2)
        if "." in strn1 or "." in strn2:
            print("In order to use greatest common divisor, BOTH inputted numbers must be an integer!")
            quit()
        else:
            result = math.gcd(n1, n2)
    elif function == "logbase":
        result = math.log(n1, n2)
    print(f"{result}")