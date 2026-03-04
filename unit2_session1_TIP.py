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
