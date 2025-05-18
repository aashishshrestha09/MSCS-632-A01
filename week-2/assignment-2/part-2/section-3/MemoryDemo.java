import java.util.ArrayList;
import java.util.List;
import java.lang.ref.Cleaner;

public class JavaMemory {

    static class MemoryDemo {
        private List<Integer> data;
        private static int instanceCount = 0;
        private final int id;

        // Cleaner for managing cleanup actions
        private static final Cleaner cleaner = Cleaner.create();
        private final Cleaner.Cleanable cleanable;

        // State class for cleanup
        private static class State implements Runnable {
            private final int id;

            State(int id) {
                this.id = id;
            }

            @Override
            public void run() {
                System.out.println("Cleaning up MemoryDemo instance " + id);
            }
        }

        public MemoryDemo() {
            this.data = new ArrayList<>();
            this.id = ++instanceCount;
            System.out.println("Created MemoryDemo instance " + id);

            // Register cleanup action
            this.cleanable = cleaner.register(this, new State(id));
        }

        public void addData(int value) {
            data.add(value);
        }

        public void printData() {
            System.out.println("Data in instance " + id + ": " + data);
        }
    }

    public static void main(String[] args) {
        MemoryDemo demo1 = new MemoryDemo();
        demo1.addData(5);
        demo1.addData(10);
        demo1.printData();

        {
            MemoryDemo demo2 = new MemoryDemo();
            demo2.addData(20);
            demo2.printData();
        }

        // Suggest garbage collection
        System.gc();

        System.out.println("Back to main.");
        System.out.println("Total Memory: " + Runtime.getRuntime().totalMemory());
        System.out.println("Free Memory: " + Runtime.getRuntime().freeMemory());
    }
}
