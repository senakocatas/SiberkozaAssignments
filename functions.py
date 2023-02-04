# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name_sk='Sam'):
    print(f'Hello {name_sk}')


# Return values
def getSum(num1_sk, num2_sk):
    total = num1_sk + num2_sk
    return total


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1_sk, num2_sk: num1_sk + num2_sk

print(getSum(10, 3))