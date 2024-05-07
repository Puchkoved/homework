def rec(n):
    if n == 1:
        return 1
    else:
        return n * rec(n - 1)


print(rec(5))


def test(*args):
    print(args)



test ('aaaaa',54,32,True)
