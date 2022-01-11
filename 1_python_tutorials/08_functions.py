# PYTHON FUNCTIONS:
# Python has many built-in functions like print(), input(), len(). Besides built-ins you can also create your own
# functions to do more specific jobs—these are called user-defined functions.
# Using the def statement is the most common way to define a function in python.

def greater_number(a, b, c):  # a, b, c are parameters
    # set logics for detect greater number
    if a > b and b > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


# ask number from user
a = int(input("write your first number: "))
b = int(input("write your second number: "))
c = int(input("write your third number: "))

# pass the fucntion and call the parameters
result = greater_number(a, b, c)
# print the greater number
print(result)
