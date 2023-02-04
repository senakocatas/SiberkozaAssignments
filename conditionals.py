# If/ Else conditions are used to decide to do something based on something being true or false

x_sk = 10
y_sk = 5

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
# if x_sk > y_sk:
#     print(f'{x_sk} is greater than {y_sk}')

# If/else
# if x_sk > y_sk:
#     print(f'{x_sk} is greater than {y_sk}')
# else:
#     print(f'{y_sk} is grater than {x_sk}')

# elif
# if x_sk > y_sk:
#     print(f'{x_sk} is greater than {y_sk}')
# elif x_sk == y_sk:
#     print(f'{x_sk} is equal to {y_sk}')
# else:
#     print(f'{y_sk} is grater than {x_sk}')

# Nested if
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than or equal to 10')

# Logical operators (and, or, not) - Used to combine conditional statements

# and
# if x_sk > 2 and x_sk <= 10:
#     print(f'{x_sk} is greater than 2 and less than or equal to 10')

# or
# if x_sk > 2 or x_sk <= 10:
#     print(f'{x_sk} is greater than 2 or less than or equal to 10')

# not
# if not(x_sk == y_sk):
#     print(f'{x_sk} is not equal to {y_sk}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

# numbers_sk = [1,2,3,4,5]

# in
# if x_sk in numbers_sk:
#     print(x_sk in numbers_sk)

# not in
# if x_sk not in numbers_sk:
#     print(x_sk not in numbers_sk)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_sk is y_sk:
    print(x_sk is y_sk)

# is not
if x_sk is not y_sk:
    print(x_sk is not y_sk)