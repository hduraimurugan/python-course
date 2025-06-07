from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Using map
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25, 36]

# Using filter
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6]

# Using reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 720 (1*2*3*4*5*6)
