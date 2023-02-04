# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_sk = 'Brad'
age_sk = 37

# Concatenate
# print('Hello, my name is ' + name_sk + ' and I am ' + age_sk)

# String Formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name_sk, age=age_sk))

# F-Strings (3.6+)
# print(f'Hello, my name is {name_sk} and I am {age_sk}')

# String Methods

s_sk = 'hello world'

# Capitalize string
print(s_sk.capitalize())

# Make all uppercase
print(s_sk.upper())

# Make all lower
print(s_sk.lower())

# Swap case
print(s_sk.swapcase())

# Get length
print(len(s_sk))

# Replace
print(s_sk.replace('world', 'everyone'))

# Count
sub_sk = 'h'
print(s_sk.count(sub_sk))

# Starts with 
print(s_sk.startswith('hello'))

# Ends with
print(s_sk.endswith('d'))

# Split into a list
print(s_sk.split())

# Find position
print(s_sk.find('r'))

# Is all alphanumeric
print(s_sk.isalnum())

# Is all alphabetic
print(s_sk.isalpha())

# Is all numeric
print(s_sk.isnumeric())
