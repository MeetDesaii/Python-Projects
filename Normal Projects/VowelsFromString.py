sentence = "Four score and seven years ago"

# Will print vowels from the sentence!
for c in sentence:
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(c)

print([c for c in sentence if c.lower() in ['a', 'e', 'i', 'o', 'u']])
