def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
try:
    user_input = input("Enter a list of numbers separated by spaces: ")
    user_list = [int(x) for x in user_input.split()]
    sorted_list = sorted(user_list)
    target_value = int(input("Enter the target value: "))
    result = binary_search(sorted_list, target_value)
    if result != -1:
        print(f"Target {target_value} found at index {result}.")
    else:
        print(f"Target {target_value} not found in the list.")
except ValueError:
    print("Invalid input. Please enter a valid list of integers.")
