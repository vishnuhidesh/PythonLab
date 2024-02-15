num_str = input("Enter a list of numbers separated by spaces: ")
numbers_list = [int(num) for num in num_str.split()]
if not numbers_list:
    print("The list is empty.")
else:
    largest = numbers_list[0]
    for num in numbers_list:
        if num > largest:
            largest = num
    print(f"The largest number in the list is: {largest}")
