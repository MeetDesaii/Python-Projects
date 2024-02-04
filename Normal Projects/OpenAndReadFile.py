# File read by File_Name
with open("OpenAndReadFile.txt", mode='r') as file:
    # Reading one line using readline() function!
    for line in file:
        print(line)

# File read by File_Path (We can write mode='r' or 'r' as a mode for this file handling)
file = open("../README.md", 'r')
# Read multiple lines using readlines() function!
data = file.readlines()

print(data)
