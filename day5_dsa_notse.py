# A pointer is just a variable that points to a position in something, usually:
# A string
# An array
# A list

# Two pointers = using TWO positions at the same time
# Usually one starts on the left
# One starts on the right
# They move towards each other

# This pattern exists because the brute force way is slow
# Brute Force:
# Reverse the string
# Compare it to the orignal
# Or compare every character with every other character

# Smarter thinking
# Compare the first and last
# Move inward
# Stop as soon as somethign does not match

# When:
# Palindrome
# Sorted array
# Move inward
# Find pair/check condition

def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1 
        right -= 1

    return True