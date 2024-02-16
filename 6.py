def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        gcd_result = gcd(num1, num2)
        lcm_result = lcm(num1, num2)
        print(f"GCD of {num1} and {num2} is: {gcd_result}")
        print(f"LCM of {num1} and {num2} is: {lcm_result}")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
if __name__ == "__main__":
    main()
