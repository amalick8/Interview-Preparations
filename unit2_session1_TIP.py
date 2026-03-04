#Problem1
#check whether all elements in a are in b
##iterate through a and check for each element in a if this is present in b
###if all are present, return True
###return False otherwise

def all_in(a, b):
    if len(a)>len(b):
        return False
    for i in a:
        if not i in b:
            return False
        else:
            return True
lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))

#Problem2
#create a dictionary to store key value pairs
#the parameters are going to be in list format because there are indices
#dictionary_name[key] = value
def create_dictionary(keys,values):
    new_dictionary = {}
    for i in range(0,len(keys)):
        new_dictionary[keys[i]] = values[i]
    return new_dictionary
keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys,values))


#Problem3
# If not target in dictionary:
#return False
#dictionary.get(key):
#print "Key "+ key,
#print "Value "+Value

def print_pair(dictionary, target):
    if not target in dictionary:
        print('That pair does not exist!')
    else:
        val = dictionary.get(target)
        print("Key: ", target)
        print("Value: ", val)

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

#Problem4
#Take in two sets of parameters that are integers
#Loop through both and add them up
#If sum or keys is larger than sum or values, return keys, vice versa
#if equal, return balanced

def keys_v_values(dictionary):
    count_values = 0
    count_keys = 0
    for k, v in dictionary.items():
        count_values += v
        count_keys += k  
    if count_values > count_keys:
        return 'Values'
    elif count_values == count_keys:
        return 'Balanced'
    else:
        return 'Keys'
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)
dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

#Problem5
#Check current_inventory if restock key is already there
#If not, add it and add a number for the updated value
#If restock key is already there then update the value
#Return the total inventory

def restock_inventory(current_inventory,restock_list):
    for i in restock_list:
        if i in current_inventory:
            current_inventory[i] += restock_list[i]
        else:
            current_inventory[i] = restock_list[i]
    return current_inventory
current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}
restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print(restock_inventory(current_inventory,restock_list))


#Problem6
#Iterate through each of the keys
#Sum all the values and add them up
#Divide the sum by the length of dictionary

def calculate_gpa(report_card):
    sum_count = 0
    for k,v in report_card.items():
        if v == "A":
            sum_count += 4
        elif v == 'B':
            sum_count += 3
        elif v == 'C':
            sum_count += 2
        elif v == 'D':
            sum_count += 1
        else:
            sum_count += 0
    return sum_count/len(report_card)
report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

#Problem7
#update current highest rating
#compare to the other value inside the dictionary


            # do you want to excahnge linkedins?
            