def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1,len(prices)):
        price = prices[i]
        profit = price - min_price
        if min_price > price:
            min_price = price
        if max_profit < profit:
            max_profit = profit
    
    return max_profit

# LC 125 - Palindrome
# You are given a string
# You must check if it reads the same forwards and backwards
# after removing certain characters

def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].alnum():
            right -= 1
            continue 
        if s[left].lower != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True
