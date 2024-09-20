# def find_even_numbers(n):
#     evens = []
#     for i in range(n + 1):
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
# print(find_even_numbers(10))


def find_odd_numbers(numbers):
    odd = []
    for i in range(numbers + 1):
        if i % 2 != 0:
            odd.append(i)
    return odd

print(find_odd_numbers(10))
