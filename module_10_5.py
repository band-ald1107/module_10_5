import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Проверка на пустую строку
                break
            all_data.append(line.strip())  # Добавляем строку в список

if __name__ == '__main__':
    # Список названий файлов
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f'{linear_duration:.6f} (линейный)')

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_duration = time.time() - start_time
    print(f'{parallel_duration:.6f} (многопроцессный)')