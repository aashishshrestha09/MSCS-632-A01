#include <iostream>
#include <variant>
#include <vector>

using VarType = std::variant<int, double, std::string>;

class Multiplier {
    int factor;
    int count;
public:
    Multiplier(int f) : factor(f), count(0) {}

    int multiply(int value) {
        count++;
        return value * factor;
    }
    int getCount() const {
        return count;
    }
};

std::string analyzeType(const VarType& data) {
    if (std::holds_alternative<int>(data)) {
        return "Integer: " + std::to_string(std::get<int>(data));
    } else if (std::holds_alternative<double>(data)) {
        return "Double: " + std::to_string(std::get<double>(data));
    } else if (std::holds_alternative<std::string>(data)) {
        return "String: " + std::get<std::string>(data);
    }
    return "Unknown Type";
}

int main() {
    Multiplier m(3);
    std::cout << m.multiply(5) << std::endl;   // 15
    std::cout << m.multiply(7) << std::endl;   // 21
    std::cout << "Function called " << m.getCount() << " times\n";

    std::vector<VarType> items = {10, std::string("hello"), 3.14};
    for (const auto& item : items) {
        std::cout << "Input analyzed: " << analyzeType(item) << std::endl;
    }
    return 0;
}
