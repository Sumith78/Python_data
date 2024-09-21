def evens_and_odds(n):
    # Initialize counters for evens and odds
    even_count = 0
    odd_count = 0
    
    # Loop through all numbers from 1 to n
    for num in range(1, n + 1):
        if num % 2 == 0:
            even_count += 1  # Increment even counter
        else:
            odd_count += 1   # Increment odd counter
    
    # Print the result
    print(f"The number of evens are {even_count}.")
    print(f"The number of odds are {odd_count}.")

# Test the function with the input 100
evens_and_odds(100)
