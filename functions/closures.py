def outer_function(msg):
    print(f"1. Outer function called with msg='{msg}'")

    def inner_function():
        print(f"3. Inner function executing (remembered msg='{msg}')")

    print("2. Returning inner_function (but not calling it yet)")
    return inner_function


print("=== Closure Example ===")
print("Calling outer_function('Hello, Closure!')...")
my_func = outer_function("Hello, Closure!")

print("\nNow calling my_func():")
my_func()  # This actually runs inner_function