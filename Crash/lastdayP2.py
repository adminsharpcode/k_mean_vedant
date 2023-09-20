def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    input_str = input_str.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return input_str == input_str[::-1]


# Example usage:
word = "racecar"
Word1 = "vedant"
Word2 = "maithili"

if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
if is_palindrome(Word1):
    print(f"'{Word1}' is a palindrome.")
else:
    print(f"'{Word1}' is not a palindrome.")
if is_palindrome(Word2):
    print(f"'{Word2}' is a palindrome.")
else:
    print(f"'{Word2}' is not a palindrome.")
