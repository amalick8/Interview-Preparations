# Sliding Window

# Problems where:
# You look at a continous chunk of something
# Use an array or string
# And you want:
# max/min
# count
# sum
# longest / shortest

# Keep a window
# Move it one step at a time
# Add the new element entering the window
# Remove the old element leaving the window
# Update the answer
# This way you slide and do not restart

# Sliding window = maintain a moving range and update it
# incrementally instead of recomputing from scratch

# If you see 'subarray', 'substring', 'contgioius',
# 'window of size k' and 'longest/shortest/maximum/minimum'
# Your brain should whipser: 'Can I slide instead of restart'

# Time complexity:
# We move pinter forward
# We move right pointer forward
# Each element is touched once or twice
# No nested loops that restart
# O(n)

def is_valid(s):
    pile = []
    match = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for char in s:
        if char in '[{(':
            pile.append(char)
        else:
            if len(pile) == 0:
               return False
            
            top = pile[-1]

            if top != match[char]:
                return False
            
            pile.pop() 
    return len(pile) == 0\
    
# A linked list node has two parts:
# A value
# A pointer to the next node

# node(1).next = node(2)
# node(2).next = node(3)
# node(3).next = None

# Reverse requires:
# 1 > 2 > 3 > None
# 3 > 2 > 1 > None

def reverse_list(head):
    if head == None:
        return None
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node 

    return prev

print(reverse_list())

# I reverse the list iteratively using three pointers.
# I traverse the list once, so the time complexity is O(n)
# I only use constant extra space, so the space complexity is O(1)

