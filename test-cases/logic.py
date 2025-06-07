def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by Zero"

# print(divide(5,6))