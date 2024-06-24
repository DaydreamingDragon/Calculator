from helper import oneNumber, twoNumbers, firstNumberInput

# Get input for one or two number functions
i = input("Do you want a function for one or two numbers (type one or two): ")
# Perform function
if i == "one":
    n1 = firstNumberInput()
    oneNumber(n1)
elif i == "two":
    n1 = firstNumberInput()
    twoNumbers(n1)
else:
    print("Please enter the number of numbers you want to perform functions on!")
    quit()