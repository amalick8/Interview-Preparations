# Problem 1 Version 1
def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")
print(count_mississippi(6))

# Problem 2 Version 1
# Return a new string where first and last index swap
# index[0] and index[-1]
def swap_ends(my_str):
    first_letter = my_str[0]
    last_letter = my_str[-1]
    new_word = last_letter + my_str[1:-1] + first_letter
    return new_word
print(swap_ends('boat'))

# Problem 3 Version 1
def is_pangram(my_str):
    my_str=my_str.lower()
    A=[]
    for l in my_str:
        if l not in A and 
    pass
