# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits_sk = ('Apples', 'Oranges', 'Grapes')
# fruits2_sk = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2_sk = ('Apples',)

# Get value
print(fruits_sk[1])

# Can't change value
# fruits_sk[0] = 'Pears'

# Delete tuple
del fruits2_sk

# Get length
print(len(fruits_sk))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set_sk = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set_sk)

# Add to set
fruits_set_sk.add('Grape')

# Remove from set 
fruits_set_sk.remove('Grape')

# Add duplicate
fruits_set_sk.add('Apples')

# Clear set
fruits_set_sk.clear()

# Delete
del fruits_set_sk

print(fruits_set_sk)