use std::collections::VecDeque;

struct MemoryDemo {
    data: VecDeque<i32>,
}

impl MemoryDemo {
    fn new() -> MemoryDemo {
        println!("Creating a new MemoryDemo instance.");
        MemoryDemo {
            data: VecDeque::new(),
        }
    }
    fn add_data(&mut self, value: i32) {
        self.data.push_back(value);
    }
    fn print_data(&self) {
        println!("Current data: {:?}", self.data);
    }
}

impl Drop for MemoryDemo {
    fn drop(&mut self) {
        println!("MemoryDemo instance is being dropped and memory is freed.");
    }
}

fn main() {
    let mut demo = MemoryDemo::new();
    demo.add_data(5);
    demo.add_data(10);
    demo.print_data();

    {
        let mut demo2 = MemoryDemo::new();
        demo2.add_data(20);
        demo2.print_data();
        // demo2 goes out of scope here, memory is automatically freed
    }

    println!("Back to main.");
}
