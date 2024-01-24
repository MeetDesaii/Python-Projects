"""
The data inside dictionaries take the form of pairs of keys and values.
"""

x = {}
print(type(x))

file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))

file_names = file_counts.keys()
file_values = file_counts.values()

print(f"File names: {file_names}\nFile values: {file_values}")
