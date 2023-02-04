# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_sk = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
# for person_sk in people_sk:
#     print(f'Current Person: {person_sk}')

# Break
# for person_sk in people_sk:
#     if person_sk == 'Sara':
#         break
#     print(f'Current Person: {person_sk}')

# Continue
# for person_sk in people_sk:
#     if person_sk == 'Sara':
#         continue
#     print(f'Current Person: {person_sk}')

# range
# for i in range(len(people_sk)):
#     print(people_sk[i])

# for i in range(0, 11):
#     print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count_sk = 0
while count_sk < 10:
    print(f'Count: {count_sk}')
    count_sk += 1