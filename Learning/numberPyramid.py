# Number of rows for the number pyramid
rows = 5

# Loop to print each row
for i in range(1, rows + 1):
    # Print spaces followed by numbers
    print(' ' * (rows - i) + ' '.join(str(j) for j in range(1, i + 1)))
