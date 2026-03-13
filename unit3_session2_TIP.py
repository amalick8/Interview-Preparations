# Version 1, Q1

#Understang:
'''
1. We take in a list of strings
2. Each string represents an integer
3. We must return these integers as a sum
'''
#plan
'''
1. Initialize a list
2. Iterate through the numbers in nums
3. Translate the strings into integers
4. Append the integers into the list
5. Do the sum of the total list
'''

def sum_of_number_strings(nums):
    total = []
    for num in nums:
        total.append(int(num))
    return sum(total)
    
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)


# Version 1, Q2

#Understang:
'''

'''
#plan
'''

'''

        