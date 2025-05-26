def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: multiply n by factorial of n-1
    else:
        return n * factorial(n-1)

# Example usage
print(factorial(5))  # Outputs 120
