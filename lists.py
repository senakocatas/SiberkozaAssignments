# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list 
numbers_sk = [1, 2, 3, 4, 5]
fruits_sk = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2_sk = list((1, 2, 3, 4, 5))

# Get a value
print(fruits_sk[1])

# Get length
print(len(fruits_sk))

# Append to list 
fruits_sk.append('Mangos')

# Remove from list 
fruits_sk.remove('Grapes')

# Insert into position
fruits_sk.insert(2, 'Strawberries')

# Change value
fruits_sk[0] = 'Blueberries'

# Remove with pop
fruits_sk.pop(2)

# Reverse list
fruits_sk.reverse()

# Sort list
fruits_sk.sort()

# Reverse sort
fruits_sk.sort(reverse=True)

print(fruits_sk)