# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person_sk = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2_sk = dict(first_name='Sara', last_name='Williams')

# Get value 
print(person_sk['first_name'])
print(person_sk.get('last_name'))

# Add Key/value
person_sk['phone'] = '555-555-5555'

# Get dict keys
print(person_sk.keys())

# Get dict items
print(person_sk.items())

# Copy dict 
person2_sk = person_sk.copy()
person2_sk['city'] = 'Boston'

# Remove item
del(person_sk['age'])
person_sk.pop('phone')

# Clear
person_sk.clear()

# Get length
print(len(person2_sk))

# List of dict
people_sk = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people_sk[1]['name'])

# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
