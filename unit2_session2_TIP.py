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













