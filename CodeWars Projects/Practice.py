def remove_every_other(my_list):
    for index in range(0, len(my_list)):
        if index % 2 != 0 and index != 0:
            del my_list[index]
        else:
            continue


print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
