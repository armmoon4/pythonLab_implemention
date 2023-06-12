try:
    # Code that may raise an exception
    x = 10 / 0  # Division by zero error
except ZeroDivisionError:
    # Exception handler for ZeroDivisionError
    print("Error: Division by zero")
else:
    # Executed if no exception occurs
    print("Division successful")
finally:
    # Cleanup or resource release
    print("Cleanup operations")

print("Continuing with the rest of the program")
