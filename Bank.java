// Before Locking
class Bank implements Runnable {

    // Shared balance (like class variable in Python)
    static int balance = 0;

    public void deposit() {
        balance += 100;
    }

    public void withdraw() {
        balance -= 100;
    }

    public int getValue() {
        return balance;
    }

    @Override
    public void run() {
        deposit();
        System.out.println(
            "Value for Thread after deposit " +
            Thread.currentThread().getName() +
            " " + getValue()
        );

        withdraw();
        System.out.println(
            "Value for Thread after withdraw " +
            Thread.currentThread().getName() +
            " " + getValue()
        );
    }
}

// AFter Locking
// class Bank implements Runnable {

//     static int balance = 0;

//     // Lock object
//     static final Object lock = new Object();

//     public void deposit() {
//         balance += 100;
//     }

//     public void withdraw() {
//         balance -= 100;
//     }

//     public int getValue() {
//         return balance;
//     }

//     @Override
//     public void run() {
//         synchronized (lock) {
//             deposit();
//             System.out.println(
//                 "Value for Thread after deposit " +
//                 Thread.currentThread().getName() +
//                 " " + getValue()
//             );

//             withdraw();
//             System.out.println(
//                 "Value for Thread after withdraw " +
//                 Thread.currentThread().getName() +
//                 " " + getValue()
//             );
//         }
//     }
// }
