public class Main {

    public static void main(String[] args) throws InterruptedException {

        Bank bankInstance = new Bank();

        Thread t1 = new Thread(bankInstance, "Thread1");
        Thread t2 = new Thread(bankInstance, "Thread2");
        Thread t3 = new Thread(bankInstance, "Thread3");

        t1.start();
        t2.start();
        t3.start();

        // Equivalent to Python join()
        t1.join();
        t2.join();
        t3.join();
    }
}
