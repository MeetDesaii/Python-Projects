import random

random_num = random.randint(0, 100)
print(random_num)

coin_toss = random.randint(0, 1)
if coin_toss == 0:
    print("\nHead!")
elif coin_toss == 1:
    print("\nTail!")
else:
    print("\nError!")
