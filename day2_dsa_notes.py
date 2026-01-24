# A string is a sequence of characters that are stored in order and you can loop
# through it one character at a time

# Strings are ordered and each character can be accessed one by one, also length matters

# Hashmaps are important because they store the counts
# Strings + hashmaps = 🔥 in interviews

# If we are checking if s contains the same letters as t
# Slow idea: for each character in s, search the entire t
# One loop inside another loop which grows very fast 

# Optimized idea: Walk through the string once, and keep track
# of what we have seen =>  O(n)

# If we count string s => O(n)
# If we count string t => O(n)
# Comparing count => O(n)

# First loop => O(n)
# Second nested loop => O(n^2)
# If the string doubles in size, the work becomes 4× slower

def valid_anagram(s,t):
    s_string = {}
    t_string = {}

    for char in s:
        if char in s_string:
            s_string[char] += 1
        else:
            s_string[char] = 1
        
    for char in t:
        if char in t_string:
            t_string[char] += 1
        else:
            t_string[char] = 1

    return s_string == t_string

print(valid_anagram('hi','ih'))


def two_sum(nums,target):
    storage = {}
    
    for i in range(len(nums)):
        num = nums[i]
        needed = target - num
        if needed in storage:
            return [storage[needed],i]
        storage[num] = i 

print(two_sum([1,2,3,4],7))
        

    
    