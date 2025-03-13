# Use of Dictionary to count the frequency of elements in list

numbers = [1, 2, 2, 2, 4, 6, 6, 7, 7, 7, 7, 6, 15, 47]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
        
print(frequency)