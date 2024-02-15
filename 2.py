n = int(input("Enter the value of n: "))
perfect_numbers = []
number = 2
while len(perfect_numbers) < n:
    divisors_sum = sum([divisor for divisor in range(1, number) if number % divisor == 0])
    if divisors_sum == number:
        perfect_numbers.append(number)
    number += 1
print(f"The first {n} perfect numbers are: {perfect_numbers}")
