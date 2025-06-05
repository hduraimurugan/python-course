class Pizza:
    # Class attribute
    pizza_types = ["margherita", "pepperoni", "vegetarian"]

    def __init__(self, size, toppings):
        # Instance attributes
        self.size = size
        self.toppings = toppings

    # Instance method - works with instance data
    def description(self):
        return f"A {self.size} pizza with {', '.join(self.toppings)}"

    # Class method - works with class-level data
    @classmethod
    def margherita(cls, size):
        return cls(size, ["tomato sauce", "mozzarella", "basil"])

    # Another class method - alternative constructor
    @classmethod
    def pepperoni(cls, size):
        return cls(size, ["tomato sauce", "mozzarella", "pepperoni"])

    # Static method - utility function
    @staticmethod
    def calculate_area(diameter):
        import math
        radius = diameter / 2
        return math.pi * radius ** 2


# Using the different method types:

# Instance method usage
my_pizza = Pizza("medium", ["mushrooms", "olives"])
print(my_pizza.description())  # A medium pizza with mushrooms, olives

# Class method usage (alternative constructors)
margherita = Pizza.margherita("large")
print(margherita.description())  # A large pizza with tomato sauce, mozzarella, basil

pepperoni = Pizza.pepperoni("small")
print(pepperoni.description())  # A small pizza with tomato sauce, mozzarella, pepperoni

# Static method usage
print(f"Area of 12-inch pizza: {Pizza.calculate_area(12):.2f} square inches")