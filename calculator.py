import math

input1 = input("Enter first number: (type pi for pi): ")
if input1 == "pi":
    n1 = math.pi
else:
    try:
        n1 = int(input1)
    except ValueError:
        try:
            n1 = float(input1)
        except ValueError:
            print("Please enter a valid decimal number or pi!")
print(f"{n1}")