# args
def sum_of(*args):
    final_sum = 0
    for num in args:
        final_sum += num
    return final_sum


print(sum_of(1, 2, 3))
print(sum_of(56, 29, 23, 58, 20, 9, 49))
print(sum_of(5, 32))
print(sum_of(50, 20, 60, 38))


# kwargs
def total_bill(**kwargs):
    total = 0
    for k, v in kwargs.items():
        total += v
    return round(total, 2)


print(total_bill(coffee=2.99, cake=4.55, juice=2.89))
print(total_bill(book=2.49, pen=0.99, pencil=0.59, textbook=45.99))
