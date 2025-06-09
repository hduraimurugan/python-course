import logging

# Set up basic logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',  # logs will be saved to this file
    filemode='w',        # overwrite file each time
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide(a, b):
    try:
        logging.info(f"Trying to divide {a} by {b}")
        result = a / b
        logging.debug(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero!")
        return "Cannot divide by zero"
    except Exception as e:
        logging.exception("Unexpected error occurred")
        return f"Error: {e}"

# Test cases
print(divide(10, 2))   # Should log success
print(divide(10, 0))   # Should log ZeroDivisionError
print(divide('10', 2)) # Should log TypeError
