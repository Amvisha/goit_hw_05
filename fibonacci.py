def caching_fibonacci():
    """
    Creates a function to calculate Fibonacci numbers using caching.

    Returns:
        function: The internal function fibonacci(n) calculates the nth Fibonacci number.
    """
    cache = {}  # Dictionary for storing calculated values

    def fibonacci(n):
        """
        Calculates nth Fibonacci numbers using caching.

        Args:
            n (int): Fibonacci number index.

        Returns:
            int: The nth Fibonacci number.
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n] # Return the value from the cache, if it exists

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Calculate and store the result in the cache
        # print('{} not in cache {}'.format(n, cache))
        return cache[n]
    return fibonacci # Returning the inner function

# Example of use:
fib = caching_fibonacci()

print(fib(10))  # Output 55
print(fib(15))  # Output 610
print(fib(14))  # Output 377 from cache
# print(caching_fibonacci()(10)) # Output 55
