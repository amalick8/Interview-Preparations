# # Version 1, Q1

# #Understang:
# '''
# 1. We take in a list of strings
# 2. Each string represents an integer
# 3. We must return these integers as a sum
# '''
# #plan
# '''
# 1. Initialize a list
# 2. Iterate through the numbers in nums
# 3. Translate the strings into integers
# 4. Append the integers into the list
# 5. Do the sum of the total list
# '''

# def sum_of_number_strings(nums):
#     total = []
#     for num in nums:
#         total.append(int(num))
#     return sum(total)
    
# nums = ["10", "20", "30"]
# sum = sum_of_number_strings(nums)
# print(sum)


# Version 1, Q2

#Understang:
'''
Take in a sorted list of integers
Remove all duplicate integers from list
Return list
'''
#plan
'''
1. Create a new dictionary
2. Loop through the list to see if the integer is already in the dictionary as a key, if not, add it. If it's there, do nothing.
3. Create a new list
4. Loop through the dictionary by keys
5. return new list
'''

# def remove_duplicates(nums):
    # d = {}
    # l = []
    # for num in nums:
    #     if num not in d:
    #         d[num] = num
    
    # for key in d:
    #     l.append(key)

#     newList = []

#     for item in nums:
#         if item  not in newList:
#             newList.append(item)
    
#     return newList

# nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))


# Version 1, Q3

#Understang:
'''
1. Write a funciton that takes a string 
2. reverse the string of the letters
3. return the new strings but all the letters should be shifted
'''
#plan
'''
1.create a function reverse_only_letters 
2. create a new string
3.loop through the spring in reverse check isalpha
s.isalpha() Returns true if all characters in given string are alphabetic letters (a-z)
4. append to the new list
5. return new list
'''

def reverse_only_letters(s):
    # newString = ""

    # for item in range(len(s)-1, -1, -1):
    #     newString += s[item]
    # return newString
    
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s) #j-Ih-gfE-dCba 