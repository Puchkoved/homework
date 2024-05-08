data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def num(l):  # Считает сумму чисел
    num0 = 0
    new_l = []
    for i in range(len(l)):
        if l[i].isdigit():
            num0 = 10 * num0 + int(l[i])
            if i + 1 < len(l):
                if l[i + 1].isdigit() == False:
                    new_l.append(num0)
            else:
                new_l.append(num0)
        else:
            num0 = 0
    return sum(new_l)


################################################################

def st(new):  # Считает кол-во символов между '' не являющихся числом
    j = 0
    k = 0
    for i in new:
        if i == "'":
            j += 1
            continue
        if j == 1 and i.isdigit() == False:
            k += 1
        if j == 2:
            j = 0
    return k


print(st(str(data_structure)) + num(str(data_structure)))
ауау