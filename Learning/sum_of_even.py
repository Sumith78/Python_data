def sum_of_even(n):
    total = 0
    for num in range(1, n + 1):
        if num % 2 == 0:
            total += num
    return total

print(sum_of_even(20))
