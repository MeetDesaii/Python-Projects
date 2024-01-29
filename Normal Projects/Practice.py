nums = [3,2,4]
target = 6

for index1, num in enumerate(nums):
    for index2, item in enumerate(nums[index1+1:]):
        if (num + item) == target:
            print(index1, index2)
            exit()
