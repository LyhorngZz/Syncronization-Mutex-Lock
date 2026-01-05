import threading 
from threading import Semaphore
import time

a = Semaphore(1)
b = Semaphore(0)
c = Semaphore(0)

def process1():
    a.acquire()
    print("H")
    print("E")
    b.release()
    b.release()

def process2():
    b.acquire()
    print("L")
    c.release()

def process3():
    c.acquire()
    c.acquire()
    print("O")

t1 = threading.Thread(target=process1)
t2 = threading.Thread(target=process2)
t3 = threading.Thread(target=process2)

t4 = threading.Thread(target=process3)


t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()