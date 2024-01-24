animals = ["Cow", "Monkey", "Lion", "Tiger", "Elephant", "Peacock", "Dolphin"]

chars = 0
for animal in animals:
    chars += len(animal)

print(f"Total characters: {chars}\nAverage length of element: {chars/len(animals)}")
