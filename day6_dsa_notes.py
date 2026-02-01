def binary_search(nums,target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1

    return -1
print(binary_search([1,3,5,7,9],9))

# You are given a string made only of these characters
# ( ) { } [ ]
# Are the paranthees properly closed and in the correct order?
# Return True if valid
# Return False if invalid

# This problem exists because:
# We need to remember what was opeend most recently
# And make sure its the first thing to be closed

# The tool we use is a stack (from zero)
# What is a stack? (No jargon)
# Think of stack like a pile of plates
# You can only:
#   put a plate on top
#   taek the top plate off
# You cannot grab from the middle
# The rule is called:
#   Last in, First out

# Start with an empty stack
# Read the string left to right
# If you can see an opening bracket:
#   Put it on the stack
# If you see a closing bracket:
#   The top of the staack must match it
#   If it doesnt -> invalid
#   If the stack is empty -> invalid
#   Otherwise -> pop the top
# 
# At the end:
#   Stack must be empty to be valid

def is_valid(s):
    pile = []
    matches = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for char in s:
        if char in '([{':
            pile.append(char)
        else:
            if len(pile) == 0:
                return False
        
            top = pile[-1]

            if top != matches[char]:
                return False
            
            pile.pop()

    return len(pile) == 0

            