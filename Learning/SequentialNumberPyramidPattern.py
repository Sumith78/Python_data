# Number of rows for the number half pyramid
rows = 5

# Variable to keep track of the current number
num = 1

# Loop to print each row
for i in range(1, rows + 1):
    # Print the numbers for each row
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()  # Move to the next line after each row
