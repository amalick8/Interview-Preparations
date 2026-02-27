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

def reverse_list(lst):
    new_list = []
    first1 = len(lst)-1
    while first1 >= 0 and first1<len(lst):
        new_list.append(lst[first1])
        first1 -=1
    return new_list
print(reverse_list([1,2,3,4,5]))

def reverse_list1(lst):
    new_list = []
    for i in range(len(lst)-1,-1,-1):
        new_list.append(lst[i])
    return new_list
print(reverse_list1([1,2,3,4,5]))

def get_evens(lst):
    new_list = []
    for num in lst:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
print(get_evens([1,2,3,4,5]))

def multiplication_table(num):
    for i in range(1,11):
        print(num*i)
multiplication_table(7)

def find_divisors(n):
    new_list = []
    for i in range(1,n+1):
        if n%i == 0:
            new_list.append(i)
    return new_list
print(find_divisors(6))



def move_zeroes(nums):
