import threading
import time
from threading import Semaphore

# -----------------------------
# Shared Resource: Bank Account
# -----------------------------
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.lock = Semaphore(1)

# Create shared resources
account1 = BankAccount("Account1", 1000)
account2 = BankAccount("Account2", 1000)

# -----------------------------
# Transfer Function
# -----------------------------
def transfer(from_account, to_account, amount):
    print(f"{threading.current_thread().name} trying to lock {from_account.name}")
    from_account.lock.acquire()
    print(f"{threading.current_thread().name} locked {from_account.name}")

    time.sleep(1)  # Force context switch (important for deadlock)

    print(f"{threading.current_thread().name} trying to lock {to_account.name}")
    to_account.lock.acquire()
    print(f"{threading.current_thread().name} locked {to_account.name}")

    # Critical section
    if from_account.balance >= amount:
        from_account.balance -= amount
        to_account.balance += amount
        print(f"Transferred {amount} from {from_account.name} to {to_account.name}")

    # Release locks (this will never be reached due to deadlock)
    to_account.lock.release()
    from_account.lock.release()

# -----------------------------
# Threads (Cause Deadlock)
# -----------------------------
t1 = threading.Thread(
    target=transfer,
    name="Thread-A",
    args=(account1, account2, 100)
)

t2 = threading.Thread(
    target=transfer,
    name="Thread-B",
    args=(account2, account1, 200)
)

# Start threads
t1.start()
t2.start()

# Join threads (program will freeze here)
t1.join()
t2.join()

print("This line will never be printed due to deadlock")
