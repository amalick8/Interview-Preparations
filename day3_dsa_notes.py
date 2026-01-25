# Hashmaps should be used when you need to:
# Count things (frequency)
# Check if something exists
# Map on thing to another
# Avoid nested loops

# Common patterns:
# 'Have I seen this before?'
# 'How many times does this appear?'
# 'What index/value matches this?'

def two_sum(nums,target):
    storage = {}

    for i in range(len(nums)):
        num = nums[i]
        needed = target - num
        if needed in storage:
            return [storage[needed],i]
        storage[num] = i

    return storage

# You are given a list of stock prices:
# prices[i] = price on day i
# You can:
# Buy once
# Sell once
# Sell after you buy
# Goal is to maximize profit

def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        profit = price - min_price
        if price < min_price:
            min_price = price
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

print(maxProfit([7,1,2,3,4,5,6]))
    