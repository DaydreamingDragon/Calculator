from helper import oneNumber, twoNumbers, firstNumberInput

# Get input for one or two number functions
i = input("Do you want a function for one or two numbers (type one or two): ")
# Make sure inputted number is a float or int
n1 = firstNumberInput()
# Perform function
if i == "one":
    oneNumber(n1)
elif i == "two":
    twoNumbers(n1)
else:
    print("Please enter the number of numbers you want to perform functions on!")
    quit()