def is_prime(func):
    def wrapper(*args):
        print(*args)
        res = func(*args)
        for i in range(2, res + 1):
            if i == res:
                print('Простое')
            elif res % i == 0:
                print('Составное')
                break
        return res

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)