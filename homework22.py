import os
import time
directory = os.getcwd()
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        print(f'Обнаружен файл: {filename}, Путь: {os.path.join(dirpath, filename)}, '
              f'Размер: {os.path.getsize(os.path.join(dirpath, filename))}, '
              f'Время изменения: {time.strftime('%d.%m.%Y %H:%M', time.gmtime(os.path.getmtime(os.path.join(dirpath, filename))))},'
              f' Родительская директория: {os.path.dirname(os.path.join(dirpath, filename))}')
        print('*'*30)



