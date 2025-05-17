#include <iostream>
#include <vector>

class MemoryDemo {
private:
    std::vector<int>* data;
    static int instanceCount;
    int id;

public:
    MemoryDemo() {
        data = new std::vector<int>();
        id = ++instanceCount;
        std::cout << "Created MemoryDemo instance " << id << std::endl;
    }

    void addData(int value) {
        data->push_back(value);
    }

    void printData() const {
        std::cout << "Data in instance " << id << ": ";
        for (int val : *data) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }

    ~MemoryDemo() {
        delete data;
        std::cout << "Deleted MemoryDemo instance " << id << " and freed memory." << std::endl;
    }
};

int MemoryDemo::instanceCount = 0;

int main() {
    MemoryDemo* demo1 = new MemoryDemo();
    demo1->addData(5);
    demo1->addData(10);
    demo1->printData();

    {
        MemoryDemo* demo2 = new MemoryDemo();
        demo2->addData(20);
        demo2->printData();
        delete demo2;  // Manual deallocation
    }

    std::cout << "Back to main." << std::endl;

    delete demo1;  // Manual deallocation

    return 0;
}
