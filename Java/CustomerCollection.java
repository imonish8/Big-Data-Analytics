import java.util.ArrayDeque;
import java.util.PriorityQueue;

class Customer {
    String name;
    int id;

    public Customer(String name, int id) {
        this.name = name;
        this.id = id;
    }

    @Override
    public String toString() {
        return "Customer{" + "name='" + name + '\'' + ", id=" + id + '}';
    }
}

class CustomerCollection {
    public static void main(String[] args) {
        // Using ArrayDeque
        ArrayDeque<Customer> deque = new ArrayDeque<>();
        deque.add(new Customer("Alice", 101));
        deque.add(new Customer("Bob", 102));
        deque.addFirst(new Customer("Eve", 103));

        System.out.println("ArrayDeque Elements: ");
        for (Customer customer : deque) {
            System.out.println(customer);
        }

        // Using PriorityQueue
        PriorityQueue<Customer> priorityQueue = new PriorityQueue<>((c1, c2) -> c1.id - c2.id);
        priorityQueue.add(new Customer("Charlie", 104));
        priorityQueue.add(new Customer("Dave", 105));

        System.out.println("\nPriorityQueue Elements: ");
        while (!priorityQueue.isEmpty()) {
            System.out.println(priorityQueue.poll());
        }
    }
}
