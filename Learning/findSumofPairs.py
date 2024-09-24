def find_pairs_with_sum(arr, target):
    pairs = []
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)
    return pairs

# Example usage:
arr = [1, 2, 3, 4, 5, 6]
target = 7
print(find_pairs_with_sum(arr, target))  # Output: [(4, 3), (5, 2), (6, 1)]
