data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def typ(obj):
    sum = 0
    if isinstance(obj, int):
        return obj
    if isinstance(obj, str):
        return len(obj)
    if isinstance(obj, dict):
        obj = list(obj.items())
    for i in obj:
         sum = sum + typ(i)
    return sum


print(typ(data_structure))