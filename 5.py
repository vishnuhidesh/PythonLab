def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
result = fibonacci(num_terms)
print(f"The Fibonacci series with {num_terms} terms is: {result}")
