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

def count_by_category(items):
    count_dictionary = {} # starts empty, keys: category, values: count #

    for item in items:
        # item is a tuple, 0, 1
        current_category = item[0]
        current_name = item[1]

        if current_category not in count_dictionary:
            # its teh first time seeing it
            count_dictionary[]
