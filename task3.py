import threading
import random
import time


data_list = []
list_filled = threading.Event()
calculate_sum_e = threading.Event()


def fill_list():
    global data_list
    for i in range(10):
        data_list.append(random.randint(1, 100))
        time.sleep(0.1)
    list_filled.set()


def calculate_sum():
    list_filled.wait()
    total_sum = sum(data_list)
    print(f"Сумма элементов списка: {total_sum}")
    calculate_sum_e.set()


def calculate_average():
    list_filled.wait()
    calculate_sum_e.wait()
    average = sum(data_list) / len(data_list)
    print(f"Среднеарифметическое значение списка: {average}")


thread_1 = threading.Thread(target=fill_list)
thread_2 = threading.Thread(target=calculate_sum)
thread_3 = threading.Thread(target=calculate_average)

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

print(f"Полученный список: {data_list}")
