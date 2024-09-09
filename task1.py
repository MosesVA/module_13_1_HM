import threading


def find_max(nums, event_for_wait, event_for_set):
    for i in range(5):
        event_for_wait.wait()
        event_for_wait.clear()
        print(f"Максимальное значение в вашем списке: {max(nums)}")
        event_for_set.set()


def find_min(nums, event_for_wait, event_for_set):
    for i in range(5):
        event_for_wait.wait()
        event_for_wait.clear()
        print(f"Минимальное значение в вашем списке: {min(nums)}")
        event_for_set.set()


event_1 = threading.Event()
event_2 = threading.Event()

numbers = [int(x) for x in input("Напишите список чисел через пробел: ").split()]

max_thread = threading.Thread(target=find_max, args=(numbers, event_1, event_2))
min_thread = threading.Thread(target=find_min, args=(numbers, event_2, event_1))

max_thread.start()
min_thread.start()

event_1.set()

max_thread.join()
min_thread.join()
