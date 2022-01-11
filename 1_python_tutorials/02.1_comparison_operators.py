# Comparison Operators
# Comparison operators are used to compare two value
# 1-   ==	   ---->  Equal
x = 5
y = 3
print(x == y)

# 2-   !=	   ---->  Not equal

x = 5
y = 3

print(x != y)

# 3-   >	   ---->  Greater than
x = 5
y = 3

print(x > y)

# 4-   <	   ---->  Less than
x = 5
y = 3

print(x < y)

# 5-   >=	   ---->  Greater than or equal to
x = 5
y = 3

print(x >= y)

# 6-   <=	   ---->  Less than or equal to
x = 5
y = 3

print(x <= y)

# example
name = input("what is your name? ")
print("Hello", name)
age = int(input("what is your age? "))
if age >= 18:
    print("you can apply for CNIC")
else:
    print("you can't apply for CNIC")
