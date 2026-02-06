# Use sliding window when:
# Array or string
# Continous
# Asking for max / min, sum / count, longest /shortest

# Window = range [left > right]
# Right pointer moves forward
# Left pointer moves forward only when needed
# Never goes backwards
# Update results while sliding

# It is fast because it enters the window once, leaves the window once:
# O(n)

# Fixed sliding window
# Window size = k
# Example: max sum of size k

# Variable size window
# Based on a condition
# Example: longest substring without repeats

def reverse_linked_list(head):
    if head == None:
        return None
    current = head
    prev = None

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Merge Two Sorted Lists (From Zero)
# You are given two linked lists that are already sorted
# List 1: 1 > 3 > 5 > None
# List 2: 2 > 4 > 6 > None
# Result: 1 > 2 > 3 > 4 > 5 > 6 > None

class ListNode: 
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1,l2):
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

# The time complexity is O(n+m) because there are two lists
# List 1 has n nodes and list 2 has m nodes. 

# A linked list is:
# a chain of boxes connected by arrows

# Each box (node) has:
# a value
# a pointer (arrow) to the next box

# 1 > 3 > 5 > None

# Why not just arrays?
# Arrays:
# Fast random access (arr[5])
# Hard to insert/remove in the middle

# Linked Lists:
# Slow random access
# Easy to arrange pointers

# In interviews, linked lists exist to test:
# Pointer logic
# Traversal
# Careful thinking

# What is a pointer in python terms:
# A pointer is just a varaible that stores where something is
# l1 = l1.next means move my reference to the next node

# How traversal works
while current:
    current = current.next 
# Walk forward until you hit None
# This is how every linked list algorithim works
# No indexes, no jumping and only arrows

# Why it feels weird:
# There is no i
# There is no len
# Everything is relevant to the current node

# Time Complexity:
# You can only move forward
# You visit nodes one by one
# 1 traversal = O(n)
# 2 traversals back to back = O(n)
# Merging two lists = O(n+m)

# Multiple traversals in sequence = linear
# Traversals inside traversals = quadratic
# O(n) vs O(n^2)

# A linked list algorithim is just walking arrows forward
# and changing where arrows point.

# Time complexity demands on how many times you walk those arrows
