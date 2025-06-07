def apply_operation(func, a, b):
    return func(a, b)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

print(apply_operation(add, 5, 3))       # Output: 8
print(apply_operation(multiply, 5, 3))  # Output: 15