print('Задача 1: Фабрика функций')


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def operation(oper, a, b):
    return oper(a, b)


try:
    print(operation(add, 8, 2))
    print(operation(sub, 8, 2))
    print(operation(mul, 8, 2))
    print(operation(div, 8, 2))
    print(operation(div, 8, 0))
except Exception as exc:
    print('Error: ', *exc.args)

print('Задача 2 лямбда')


def sq(num):
    return num ** 2


result = lambda num: num ** 2
print(result(4))
print(sq(4))

print('Задача 3: Вызываемые объекты')
class Rect:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, *args, **kwargs):
        return self.a * self.b


p = Rect(2, 4)
print(p())
