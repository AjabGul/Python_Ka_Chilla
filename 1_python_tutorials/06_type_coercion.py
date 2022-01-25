# There are two type of data type conversion
# 1: implicit type conversion and 2: expicit type conversion


# 1- IMPLICITE TYPE Coercion:
# Python automatically converts one data type to another data type.
# This process doesn't need any user involvement.
# Let's see an example where Python promotes the conversion of the lower data type (integer)
#  to the higher data type (float) to avoid data loss.

x = 4
y = 4.5
z = "Hello"

print(type(x))  # int
print(type(y))  # float
print(type(z))  # string

x = x * y  # converted to float
print(x, "x data type is ", type(x))

# 2: EXPLICIT TYPE COERCION
# Explicit Type Conversion, users convert the data type of an object to required data type.
# We use the predefined functions like int() , float() , str() , etc to perform explicit type conversion.
# This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

# example

age = input("what is your age? ")  # string
print(type(age))
age = int(age)
print(type(age))  # converted to int
