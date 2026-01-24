def char_frequency(s): # Im making a function that receives a string called s
    freq = {} # This is my memory box

    for char in s: # Go through the string one character at a time
        if char not in freq: # Have I seen this character before?
            freq[char] = 1 # If not, I will assign it one
        else:
            freq[char] += 1 # If I have, I will increase the count

    return freq # Give back the final count

####
def contains_duplicate(nums):
    seen = set() # We only need to remember seen or not seen

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

print(contains_duplicate([1,2,3,1]))

####
def is_anagram(s,t):
    s_chars = {}
    t_chars = {}
    for char in s:
        if char not in s_chars:
            s_chars[char] = 1
        else:
            s_chars[char] += 1
# After first loop: s_chars = {'a':3, 'n':1, 'g':1, 'r':1, 'm':1}
    for char in t:
        if char not in t_chars:
            t_chars[char] = 1
        else:
            t_chars[char] += 1
# After second loop: t_chars = {'n':1, 'a':3, 'g':1, 'r':1, 'm':1}

    return s_chars == t_chars
# Order does not matter in dictionaries, only key/value pairs

print(is_anagram('anagram','nagaram'))
        
# One loop is O(n)
# Loop inside loop is O(n^2)



