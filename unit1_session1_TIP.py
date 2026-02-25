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


