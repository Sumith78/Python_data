def find_missing_numbers(arr):
    n = len(arr) + len(set(range(1, len(arr) + 1)))  # The maximum possible value of n
    full_set = set(range(1, n + 1))  # Set of all numbers from 1 to n
    arr_set = set(arr)  # Set of numbers present in the array
    missing_numbers = sorted(full_set - arr_set)  # Find the difference and sort the result
    return missing_numbers

# Example usage
arr = [1, 2, 4, 6, 7, 9]
print(f"The missing numbers are: {find_missing_numbers(arr)}")


