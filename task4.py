import threading
import random
import math
import time

file_path = 'numbers.txt'
file_filled = threading.Event()


def fill_file(filename):
    print('Заполняю файл случайными числами...')
    with open(filename, 'w') as file:
        for i in range(10):
            file.write(f"{random.randint(1, 20)}\n")
            time.sleep(0.5)
    print("Файл заполнен случайными числами.")
    file_filled.set()


def find_primes(filename):
    file_filled.wait()
    print('Записываю простые числа в файл primes.txt...')
    primes = []
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        for number in numbers:
            if number > 1:
                is_prime = all(number % i != 0 for i in range(2, int(math.sqrt(number)) + 1))
                if is_prime:
                    primes.append(number)
    with open('primes.txt', 'w') as file:
        for prime in primes:
            file.write(f"{prime}\n")
            time.sleep(0.5)
    print("Простые числа записаны в файл primes.txt.")


def calculate_factorials(filename):
    file_filled.wait()
    time.sleep(0.2)
    print('Записываю факториалы в файл factorials.txt...')
    factorials = []
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
        for number in numbers:
            factorial = math.factorial(number)
            factorials.append((number, factorial))
    with open('factorials.txt', 'w') as file:
        for number, factorial in factorials:
            file.write(f"{number}: {factorial}\n")
            time.sleep(0.5)
    print("Факториалы записаны в файл factorials.txt.")


thread_1 = threading.Thread(target=fill_file, args=(file_path,))
thread_2 = threading.Thread(target=find_primes, args=(file_path,))
thread_3 = threading.Thread(target=calculate_factorials, args=(file_path,))

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

print("Все операции завершены.")
