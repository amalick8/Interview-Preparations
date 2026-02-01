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

def binary_search(nums,target):
    left = 0
    right = len(nums) - 1
    

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

# Time complexity:
# How long does the alogirithim take as the input gets bigger
# How many steps does it take
# How many operations do we do
# O(n): Check everything once
# O(n^2): Nested loops (slow)
# O(log n): cut in half each time 

# Space complexity: 
# How much extra memory does this use
# We only count the extra memory
# Using a few variables = O(1) space
# Creating a new array or hashmap = O(n) space
# Uses left, right and mid