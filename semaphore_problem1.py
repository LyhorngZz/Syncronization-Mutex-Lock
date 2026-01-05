import threading
import time
from threading import Semaphore

empty_pairs = Semaphore(50)
full_pairs = Semaphore(0)
mutex = Semaphore(1)

buffer = []

def producer(pid):
    while True:
        # Produce a particle pair
        p1 = f"P{pid}-1"
        p2 = f"P{pid}-2"

        empty_pairs.acquire()     # WAIT(emptyPairs)
        mutex.acquire()           # WAIT(mutex)

        buffer.append(p1)
        buffer.append(p2)
        print(f"Producer {pid} produced {p1}, {p2}")

        mutex.release()           # SIGNAL(mutex)
        full_pairs.release()      # SIGNAL(fullPairs)

        time.sleep(1)

def consumer():
    while True:
        full_pairs.acquire()      # WAIT(fullPairs)
        mutex.acquire()           # WAIT(mutex)

        p1 = buffer.pop(0)
        p2 = buffer.pop(0)
        print(f"Consumer packaged {p1} and {p2}")

        mutex.release()           # SIGNAL(mutex)
        empty_pairs.release()     # SIGNAL(emptyPairs)

        time.sleep(2)

# Start multiple producers
for i in range(3):
    threading.Thread(target=producer, args=(i+1,), daemon=True).start()

# Start single consumer
threading.Thread(target=consumer, daemon=True).start()

time.sleep(20)
