# Number of rows for the number half pyramid
rows = 5

# Loop to print each row
for i in range(1, rows + 1):
    # Print numbers from 1 to i
    print(' '.join(str(j) for j in range(1, i + 1)))
