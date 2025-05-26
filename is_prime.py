def is_prime(n):
    """Function to check if n is a prime number"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(10)) # Outputs: False
print(is_prime(11)) # Outputs: True
