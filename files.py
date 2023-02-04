# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile_sk = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile_sk.name)
print('Is Closed: ', myFile_sk.closed)
print('Opening Mode: ', myFile_sk.mode)

# Write to file
myFile_sk.write('I love Python')
myFile_sk.write(' and JavaScript')
myFile_sk.close()

# Append to file
myFile_sk = open('myfile.txt', 'a')
myFile_sk.write(' I also like PHP')
myFile_sk.close()

# Read from file
myFile_sk = open('myfile.txt', 'r+')
text_sk = myFile_sk.read(100)
print(text_sk)