name = input("Please enter your name: ")

with open(f"CreateAndWriteFile_{name}PyFile.txt", 'w') as file:
    file.write(f"Welcome {name}, new file created successfully!")
    file.writelines(["\nWelcome to the huge python directory!", "\nLet's dive into AI with all basic understanding of Python!"])


with open(f"CreateAndWriteFile_{name}PyFile.txt", 'r+') as file:
    data = file.read()

    print(data)
