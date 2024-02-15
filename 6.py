def calculate_gcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)
def calculate_lcm(x, y):
    gcd = calculate_gcd(x, y)
    lcm = abs(x * y) // gcd
    return lcm
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd_result = calculate_gcd(num1, num2)
lcm_result = calculate_lcm(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
