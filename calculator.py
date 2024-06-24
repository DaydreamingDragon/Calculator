import math
import helper.py

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

# Get input for one or two number functions
i = input("Do you want a function for one or two numbers (type one or two): ")
if i == "one":
    oneNumber(n1)
elif i == "two":
    twoNumbers(n1)
else:
    print("Please enter the number of numbers you want to perform functions on!")
    quit()