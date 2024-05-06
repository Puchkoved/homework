def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2)
print_params(2, 25)
print_params(2, 25, [1, 2, 3])

values_list = (1, 'txt', False)
values_dict = {'a': 2, 'b': 'string', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['st', 5]
print_params(*values_list_2, 42)
