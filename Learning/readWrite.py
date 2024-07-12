# Writing to a file
with open('example.txt', 'w') as file:
  create=  file.write('Hello, world!')
  print(create)

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()

# Printing the content read from the file
print(content)

# You can use the open() function to read and write files in Python.
# The 'w' mode is used for writing, which creates the file if it doesn't exist
# and truncates the file if it does. The 'r' mode is used for reading.
