# nums = [3, 7, 10, 9, 45, 32, 12, 78, 34, 98, 35, 76, 83, 40, 50]
# largest = 0
# for num in nums:
#     if largest <= num:
#         largest = num
#
# print("The largest number is: {}".format(largest))

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)

        if largest is None and smallest is None:
            largest = number
            smallest = number
        else:
            if number > largest:
                largest = number
            elif number < smallest:
                smallest = number

    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
