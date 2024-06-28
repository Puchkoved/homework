l = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def filters(num):
    return num % 2


new_l = list(map(lambda x: x ** 2, filter(filters, l)))
print(new_l)