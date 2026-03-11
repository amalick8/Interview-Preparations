# Problem 1 Version 1
def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")
print(count_mississippi(6))

# Problem 2 Version 1
# Return a new string where first and last index swap
# index[0] and index[-1]
def swap_ends(my_str):
    first_letter = my_str[0]
    last_letter = my_str[-1]
    new_word = last_letter + my_str[1:-1] + first_letter
    return new_word
print(swap_ends('boat'))

# Problem 3 Version 1
def is_pangram(my_str):
    my_str=my_str.lower()
    A=[]
    for l in my_str:
        if l not in A and l.isalpha():
            A.append(l)
        else:
            pass
    return len(A)==26
str2 = "The dog jumped"
print(is_pangram(str2))

# Problem 4 Version 1
def reverse_string(my_str):
    return my_str[::-1]
print(reverse_string('hello'))
      
# Problem 5 Version 1
# Find the first non repeating character
# Return this characters index
def first_unique_char(my_str):
    dict = {}
    for letter in my_str:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    
    for key, value in dict.items():
        if value == 1:
            return my_str.index(key)
    return -1

print(first_unique_char('leetcode'))
print(first_unique_char('loveleetcode'))

# Problem 6 Version 1
def min_distance(words, word1, word2):
words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)
words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)


