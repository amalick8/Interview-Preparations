#check whether all elements in a are in b
##iterate through a and check for each element in a if this is present in b
###if all are present, return True
###return False otherwise

def all_in(a, b):
    if len(a)>len(b):
        return False

    counter = 0
    for i in a:
        if i in b:
            counter += 1
        if counter == len(a):
            return True
        else:
            return False
lst_1 = [1, 2]
lst_2 = [1, 2, 3]
print(all_in(lst_1, lst_2))
print(all_in(lst_2, lst_1))