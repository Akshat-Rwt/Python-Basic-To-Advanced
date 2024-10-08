import os

# Get the current working directory
directory = os.getcwd()

# List the contents of the directory
contents = os.listdir(directory)

# Print the contents
for item in contents:
    print(item)
