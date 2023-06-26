import re
def is_palindrome(text):
    cleaned_text = re.sub(r'[^\w]', '', text.lower())
    reversed_text = cleaned_text[::-1]
    return cleaned_text == reversed_text

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("racecar"))
print(is_palindrome("Hello, world!"))
print(is_palindrome("Step on no pets"))