import threading
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово №{i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
stop = time.time()
print(stop-start)
start = time.time()
thr1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thr2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thr3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thr4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr1.join()
thr2.join()
thr3.join()
thr4.join()
stop = time.time()
print(stop-start)
