def multiplier_factory(factor):
    count = 0  # enclosed variable in closure
    
    def multiplier(value):
        nonlocal count
        count += 1
        return value * factor
    
    def get_count():
        return count
    
    return multiplier, get_count

def analyze_type(data):
    if isinstance(data, (int, float)):
        return f"Number: {data}"
    elif isinstance(data, str):
        return f"String: {data}"
    else:
        return "Unknown Type"

if __name__ == "__main__":
    multiply_by_3, get_calls = multiplier_factory(3)
    print(multiply_by_3(5))         # 15
    print(multiply_by_3(7))         # 21
    print(f"Function called {get_calls()} times")  # 2
    
    # Dynamic typing demonstration
    for item in [10, "hello", 3.14, [1, 2]]:
        print(f"Input: {item}, Analyzed: {analyze_type(item)}")
