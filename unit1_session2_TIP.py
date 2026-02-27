def above_threshold(nums,threshold):
    output = []
    for i in nums:
        if i > threshold:
            output.append(i)
    return output
print(above_threshold([8,2,13,11,4,10,14],10))

def print_list(lst):
    for i in lst:
        print(i)
(print_list(["squirtle", "gengar", "charizard", "pikachu"]))

def average(scores):
    total = 0
    for i in scores:
        total += i
    average = total/len(scores)
    return average
print(average([84,73,92,95,88]))

def double(list):
    new_list = []
    for num in list:
        new_list += [num*2]
    return new_list
print(double([2,4,5]))

lst = [5,2,3,9,10]
def check_num(lst,nums):
    if nums in lst:
        return True
    else:
        return False
print(check_num([5,2,3,9,10],9))
print(check_num([5,2,3,9,10],4))

def max_difference(lst):
    sorted_lst = sorted(lst)
    return lst[-1]-lst[0]
print(max_difference([1,2,3,4,5]))




   
            







        

    




