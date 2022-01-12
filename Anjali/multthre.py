"""
Multi tasking -> MultiThreading
threading.Thread(function,1)
"""

import threading
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(threadName, time.time_ns())


t1 = threading.Thread(target=print_time, args=("t1", 1,))
t2 = threading.Thread(target=print_time, args=("t2", 3,))
t1.start()
t2.start()
