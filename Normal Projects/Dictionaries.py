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

company_heads = {
    "CEO": {"Name": "Meet Desai", "Age": "23", "Specialist": "Data Scientist and Project Manager"},
    "CTO": {"Name": "Abhi Bhanderi", "Age": "17", "Specialist": "Full Stack Developer"},
    "CFO": {"Name": "Vishal Bhanderi", "Age": "26", "Specialist": "Android Developer and R & D Manager"},
    "CMO": {"Name": "Preet Desai", "Age": "20", "Specialist": "Marketing Manager"}
}

print("\n\nCOMPANY EXECUTIVES:")
for position, executive_info in company_heads.items():
    print(f"\n{position}: {executive_info}")
    for key, value in executive_info.items():
        print(f"{key}: {value}")
        
        
# Dictionary Comprehensions
even_squares = {x:x**2 for x in range(101) if x%2==0}
print(f"\n\nSquares of even numbers using Dictionary Comprehension: {even_squares}")