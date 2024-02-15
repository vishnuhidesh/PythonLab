def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
def find_primes(numbers):
    return [num for num in numbers if is_prime(num)]
num_str = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in num_str.split()]
prime_numbers = find_primes(numbers_list)
print(f"The prime numbers in the list are: {prime_numbers}")
