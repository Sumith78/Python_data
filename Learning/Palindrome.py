def is_palindrome(s):
    if isinstance(s, str):  # Check if the input is a string
        if s == s[::-1]:
            return "is Palindrome"
        else:
            return "is not palindrome"
    else:
        return "Input is not a string"

# Example usage
s = "madam"
result = is_palindrome(s)
print(result)
