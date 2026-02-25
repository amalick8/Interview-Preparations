def hello_world():
    print('Hello World!')
hello_world()

def todays_mood():
    mood = "😭"
    print("Today's mood: " + mood)
todays_mood()

def print_menu(menu):
    print("Lunch today is: " + menu)
print_menu('🍕')

def sum(a,b):
    return a + b
print(sum(3,4))

def product(a,b):
    return a*b
print(product(22,7))

def classify_age(age):
    if age < 18:
        return 'child'
    else:
        return 'adult'
print(classify_age(18))
print(classify_age(7))
print(classify_age(50))

def what_time_is_it(hour):
    if hour == 2:
        return 'taco time'
    elif hour == 12:
        return 'peanut butter jelly time'
    else:
        return 'nap time'
print(what_time_is_it(2))
print(what_time_is_it(7))
print(what_time_is_it(12))

def blackjack(score):
    if score == 21:
        return 'Blackjack!'
    elif score > 21:
        return 'Bust!'
    elif score >= 17 and score < 21:
        return 'Nice hand!'
    else:
        return 'Hit me!'
print(blackjack(21))
print(blackjack(24))
print(blackjack(19))
print(blackjack(10))

def get_first(list):
    if len(list) >= 1:
        return list[0]
    else:
        return None
print(get_first([1,2,3]))
print(get_first([]))

def get_last(list):
    if len(list) >= 1:
        return list[-1]
    else:
        return None
print(get_last([1,2,3]))
print(get_last([]))

def counter(stop):
    for i in range(1,stop+1):
        print(i) 
print(counter(7))

def sum_ten():
    storage = 0
    for i in range(0,11):
        storage += i
    return storage
print(sum_ten())

def sum_positive_range(stop):
    storage = 0
    for i in range(0,stop+1):
        storage += i
    return storage
print(sum_positive_range(6))

def sum_range(start,stop):
    storage = 0
    for i in range(start,stop+1):
        storage += i
    return storage
print(sum_range(3,9))

def print_negatives(lst):
    for i in lst:
        if i < 0:
            print(i)
print(print_negatives([3,-2,2,1,-5]))
print(print_negatives([1,2,3,4,5]))

def greet_user(name):
    print(f'Hello {name}!')
greet_user('Michael')

def difference(a,b):
    return a - b
print(difference(8,3))

def concatenate_list(nums):
    return nums+nums
print(concatenate_list([1,2,3,4]))

def sleep_assessment(hours):
    if hours < 8:
        return "Oof, go back to bed!"
    elif hours >= 8 and hours <= 10:
        return "You got a good night's rest!"
    else: 
        return "You're a sleep prodigy!"
print(sleep_assessment(10))
print(sleep_assessment(4))
print(sleep_assessment(12))
print(sleep_assessment(9))

def calculate_tip(bill,service_quality):
    if service_quality == 'poor':
        return bill * 0.10
    elif service_quality == 'average':
        return bill * 0.15
    elif service_quality == 'excellent':
        return bill * 0.20
    else:
        return None
tip1 = calculate_tip(44.53, "average")
print(tip1)
tip2 = calculate_tip(44.53, "poor")
print(tip2)
tip3 = calculate_tip(44.53, "excellent")
print(tip3)

def rock_paper_scissors(player1,player2):
    if player1 == 'rock' and player2 == 'scissors':
        return 'Player1 wins'
    elif player1 == 'scissors' and player2 == 'paper':
        return 'Player1 wins'
    elif player1 == 'paper' and player2 == 'rock':
        return 'Player1 wins'
    elif player1 == player2:
        return 'Tie'
    if player1 == 'rock' and player2 == 'paper':
        return 'Player2 wins'
    elif player1 == 'paper' and player2 == 'scissors':
        return 'Player2 wins'
    elif player1 == 'scissors' and player2 == 'rock':
        return 'Player2 wins'
print(rock_paper_scissors("rock", "rock"))
rock_paper_scissors("rock", "rock")
print(rock_paper_scissors("scissors", "rock"))
print(rock_paper_scissors("scissors", "paper"))
print(rock_paper_scissors("rock", "paper"))
print(rock_paper_scissors("paper", "rock"))
    
def halve_lst(lst):
    result = []
    for number in lst:
        halved = number//2
        result.append(halved)
    return result
print(halve_lst([2,4,6,8]))

def above_threshold(lst,threshold):
    storage = []
    for number in lst:
        if number > threshold:
            storage.append(number)
    return storage
lst = [8,2,13,11,4,10,14]
result = above_threshold(lst, 10)
print(result)

def countdown(m,n):
    for i in range(m,n-1,-1):
        print(i)
print(countdown(5,1))

def power(base,exponent):
    return base**exponent
print(power(2,3))

def list_length(lst):
    count = 0
    for item in lst:
        count += 1
    return count
print(list_length([2,4,6,8,10]))

def factorial(n):
    count = 1
    for i in range(n,1,-1):
        count = count * i
    return count
print(factorial(3))

def squares(nums):
    square_list = []
    for num in nums:
        square_list.append(num**2)
    return square_list
print(squares([1,2,3,4]))

def multiply_list(lst,multiplier):
    new_list = []
    for num in lst:
        new_list.append(num*multiplier)
    return new_list
print(multiply_list([1,2,3],3))

