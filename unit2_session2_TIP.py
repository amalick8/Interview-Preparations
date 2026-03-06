'''
Input: tuples, always same size, 0 category, 1 value (item)
Output: dictionary, keys, categories, values will be count
Logic: want to group and count by category
'''

# Plan (hint: how do we use dictionaries to group things together)

'''
1. Initialize our count_dictionary {}
2. In a foor loop we check if there is a new count
3. If so we will intialize
4. If not we will increment the existing count
'''

'''def count_by_category(items):
    count_dictionary = {} # starts empty, keys: category, values: count #

    for item in items:
        # item is a tuple, 0, 1
        current_category = item[0]

        if current_category not in count_dictionary:
            # its teh first time seeing it
            count_dictionary[current_category] = 1
        else:
            count_dictionary[current_category] += 1

    return count_dictionary

items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
print(count_by_category(items))'''


'''print("Problem 1 here")
def cast_vote(votes, candidate): 
    if candidate not in votes:
        votes[candidate] = 1
    else:
        votes[candidate] += 1
    return votes
votes = {"Alice": 5, "Bob": 3}
print(cast_vote(votes, "Gina"))'''

'''
print('Problem 2 here')
# 1. We will be provided 2 dictionaries
# 2. Whichever keys are common in the dictionaries, will be outputted

# Steps
# Iterate through one dictionary using the other dictionaries key
# Return if key found in secondary dictionary

def common_keys(dict1, dict2):
    common_key_types = []
    for key in dict1:
        if key in dict2:
            common_key_types.append(key) 
    return common_key_types
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
'''

print("This is problem 3 here")

'''Write a function that takes in a list of integers nums
and counts the number of occurrences of each integer. 
The function returns the result as a dictionary with integers as keys and their counts as values.'''

def count_occurrences(nums):


#Provided with a list of integers, I need to find how often each occurs
#1. create an emoty dictionary 
#2.interate through the list of integers
#3.Count how many times each integer occurs
#return the count as a dictionary 

    '''
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] +=1
    return count
print(count_occurrences([1, 2, 2, 3, 3, 3, 4]))
# Input: nums = [1, 2, 2, 3, 3, 3, 4]
# Output: {1: 1, 2: 2, 3: 3, 4: 1}
'''


print("Problem 4 here")
#So we're being given a dictionary 









