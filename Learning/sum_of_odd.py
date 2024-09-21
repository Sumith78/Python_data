# Function to sum all odd numbers up to a given number
def sum_of_odds(n):
    """
    This function takes a number and returns the sum of all odd numbers in the range from 1 to n.

    :param n: upper limit for summing odd numbers (inclusive)
    :return: sum of odd numbers from 1 to n
    """
    total = 0  # Initialize sum
    for num in range(1, n + 1):
        if num % 2 != 0:  # Check if the number is odd
            total += num   # Add odd number to the total
    return total

# Example usage
print(sum_of_odds(10))
# Output: 25 (1 + 3 + 5 + 7 + 9)

print(sum_of_odds(15))
# Output: 64 (1 + 3 + 5 + 7 + 9 + 11 + 13 + 15)
