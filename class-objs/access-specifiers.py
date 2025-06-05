class MyClass:
    def __init__(self):
        self.public_var = "I'm public"  # Public attribute
        self._protected_var = "I'm protected"  # Protected (convention)
        self.__private_var = "I'm private"  # Private (name mangling)

    # Public method
    def public_method(self):
        print("This is a public method")
        print(f"Accessing private var inside class: {self.__private_var}")

    # Protected method (convention)
    def _protected_method(self):
        print("This is a protected method")

    # Private method (name mangling)
    def __private_method(self):
        print("This is a private method")

    # Method to access private members externally if needed
    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value


class DerivedClass(MyClass):
    def __init__(self):
        super().__init__()

    def show_protected(self):
        print(f"Accessing protected var from derived class: {self._protected_var}")

    def try_private(self):
        # This will fail - private members can't be accessed directly in derived class
        try:
            print(self.__private_var)
        except AttributeError as e:
            print(f"Error accessing private var: {e}")


# Main program to demonstrate access
def main():
    # Create instance of MyClass
    obj = MyClass()

    # Accessing public members - no restrictions
    print("\n--- Public Access ---")
    print(obj.public_var)
    obj.public_method()

    # Accessing protected members - convention says "don't do this", but you can
    print("\n--- Protected Access ---")
    print(obj._protected_var)  # Works but not recommended
    obj._protected_method()  # Works but not recommended

    # Accessing private members - name mangling makes this harder
    print("\n--- Private Access ---")
    # This would cause an AttributeError:
    # print(obj.__private_var)

    # But we can see it exists with name mangling:
    print("Private var with name mangling:", obj._MyClass__private_var)

    # Proper way to access private members is through getter/setter
    print("Private var via getter:", obj.get_private_var())
    obj.set_private_var("New private value")
    print("Modified private var:", obj.get_private_var())

    # Demonstrate access in derived class
    print("\n--- Derived Class Access ---")
    derived = DerivedClass()
    derived.show_protected()
    derived.try_private()

    # Demonstrate that private methods are also inaccessible
    try:
        obj.__private_method()
    except AttributeError as e:
        print(f"Error accessing private method: {e}")


if __name__ == "__main__":
    main()