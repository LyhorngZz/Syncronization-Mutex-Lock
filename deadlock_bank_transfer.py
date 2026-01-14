import threading
import time
from threading import Semaphore

class BankAccount:
    def __init__(self, acc_id, balance):
        self.acc_id = acc_id
        self.balance = balance
        self.lock = Semaphore(1)

def transfer(account1, account2, amount):
    # Establish fixed ordering
    first = account1 if account1.acc_id < account2.acc_id else account2
    second = account2 if account1.acc_id < account2.acc_id else account1

    print(f"{threading.current_thread().name} locking Account {first.acc_id}")
    first.lock.acquire()

    time.sleep(1)  # force context switch

    print(f"{threading.current_thread().name} locking Account {second.acc_id}")
    second.lock.acquire()

    # Critical section
    if account1.balance >= amount:
        account1.balance -= amount
        account2.balance += amount
        print(f"{threading.current_thread().name} transferred {amount} "
            f"from Account {account1.acc_id} to Account {account2.acc_id}")

    # Release in reverse order
    second.lock.release()
    first.lock.release()

account6004 = BankAccount(6004, 1000)
account6005 = BankAccount(6005, 1000)

t1 = threading.Thread(
    target=transfer,
    name="ATM-1",
    args=(account6005, account6004, 50)
)

t2 = threading.Thread(
    target=transfer,
    name="ATM-2",
    args=(account6004, account6005, 50)
)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final balances:")
print("Account 6004:", account6004.balance)
print("Account 6005:", account6005.balance)
