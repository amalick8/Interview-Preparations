class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def merged_sorted_list(l1,l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next

# Stacks
# A stack is a container where:
# The last thing you put is the first thing you take out
# Last in, First out

# Think of a stack of plates
# You put a plate on top
# You remove the top plate only
# You can't pull one from the middle
# So last plate added = first plate removed

# Operations of a stack
# Push add to the top
# Pop remove from the top
# Peep/top means to look at the top
# Is it empty?

# We implement by using a list
# stack = []
# Push:
# stack.append(x)
# Pop:
# stack.pop()
# Peep:
# stack[-1]

# Uses of stacks
# undo/redo
# backtracking
# Expression evaluation
# Parantheses check
# Function calls (call stack)

