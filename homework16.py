class Building:
    total = 0

    def __init__(self):
        Building.total += 1


objs = [Building() for i in range(40)]

print(objs, Building.total)
