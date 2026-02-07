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

# STACKS

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

# QUEUES

# A queue is a container where:
# The first thing you put in is the first you take out
# The rule is called:
# FIFO - First in, First out

# Think of a line at a store:
# First person in line > served first
# New people go to the back
# You can't skip the line

# Operations of a Queue
# Enqueue > add to back
# Dequeue > remove from front
# Front/Peek > Look at first element
# Is empty?

# Stack - LIFO - Plates
# Queue - FIFO - Line

# Fastest way
# from collections import deque
# queue = deque()
# queue.append(x) # equeue
# queue.popleft() # dequeue

# Queues are used when order of arrival matters:
# Task scheduling
# Pring jobs
# BFS (graph traversal)
# Customer service systems

def merge(nums1, m, nums2, n):
    for num in range(len(nums1)-1):
        if nums1[num] == 0:
            nums1.pop(num)
    for num in range(len(nums2)-1):
        if nums2[num] == 0:
            nums2.pop(num)
    
    new_list = nums1 + nums2
    new_list.sort()
    return new_list

