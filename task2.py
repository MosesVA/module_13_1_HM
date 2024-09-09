import threading


def find_sum(nums, event_for_wait, event_for_set):
    for i in range(5):
        event_for_wait.wait()
        event_for_wait.clear()
        print(f"Сумма чисел в вашем списке: {sum(nums)}")
        event_for_set.set()


def find_average(nums, event_for_wait, event_for_set):
    for i in range(5):
        event_for_wait.wait()
        event_for_wait.clear()
        print(f"Среднее арифметическое в вашем списке: {sum(nums) // len(nums)}")
        event_for_set.set()


event_1 = threading.Event()
event_2 = threading.Event()

numbers = [int(x) for x in input("Напишите список чисел через пробел: ").split()]

sum_thread = threading.Thread(target=find_sum, args=(numbers, event_1, event_2))
average_thread = threading.Thread(target=find_average, args=(numbers, event_2, event_1))

sum_thread.start()
average_thread.start()

event_1.set()

sum_thread.join()
average_thread.join()
