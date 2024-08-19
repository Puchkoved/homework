import pandas as pd
import time
import matplotlib.pyplot as pl

pl.ion()


def add_labels(x, y):
    for i in range(len(x)):
        pl.text(i, y[i], y[i], ha='center')


def y_data(year, x):
    y1 = list(tabl[year])
    y2 = list(tabl[year + 1])
    del_y = [(y2[j] - y1[j]) / 100 for j in range(len(y2))]
    for k in range(100):
        y = [round(y1[j] + k * del_y[j], 3) for j in range(len(y1))]
        anim(year, x, y)


def anim(year, x, y):
    pl.clf()
    pl.xlabel('Язык програмирования')
    pl.ylabel('Количество пользователей')
    fig.suptitle(f'Популярность языков програмирования в {year}')
    pl.bar(x, y)
    add_labels(x, y)
    pl.draw()
    pl.gcf().canvas.flush_events()
    time.sleep(0.02)


fig = pl.figure(figsize=(10, 5))
tabl = pd.read_excel('Данные.xls')
x = list(tabl[0])
for i in range(2019, 2022):
    y_data(i, x)
y = list(tabl[2022])
anim(2022, x, y)
pl.ioff()
pl.show()
