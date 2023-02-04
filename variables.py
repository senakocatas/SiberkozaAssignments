# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x_sk = 1          # int
# y_sk = 2.5        # float
# name_sk = 'John'  # str
# is_cool_sk = True # bool

# Multiple assignment
x_sk, y_sk, name_sk, is_cool_sk = (1, 2.5, 'John', True)

# Basic math
a_sk = x_sk + y_sk

# Casting
x_sk = str(x_sk)
y_sk = int(y_sk)
z_sk = float(y_sk)

print(type(z_sk), z_sk)