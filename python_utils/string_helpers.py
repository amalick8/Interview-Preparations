def char_frequency(s):
    freq = {}

    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    return freq

# using the first function inside the second function
def is_anagram(s,t):
    if len(s) != len(t):
        return False
    return char_frequency(s) == char_frequency(t)

def test_is_anagram():
    assert is_anagram('anagram','nagaram') == True
    assert is_anagram('rat','car') == False


def contains_duplicates(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

def two_sum_indices(nums,target):
    storage = {}

    for i in range(len(nums)):
        num = nums[i]
        needed = target - num
        if needed in storage:
            return [storage[needed],i]
        storage[num] = i

    return []

def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(len(prices)):
        price = prices[i]
        profit = price - min_price
        if min_price > price:
            min_price = price
        if max_profit < profit:
            max_profit = profit

    return max_profit

def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True


def binary_search(nums,target):
    if not is_sorted(nums):
        return -1
        
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True 

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

        
def test_max_profit():
    assert max_profit([7,1,5,3,6,4]) == 5

if __name__ == "__main__":
    print(char_frequency('hello'))
    print(is_anagram('anagram','nagaram'))
    print(is_anagram('rat','car'))
    print(contains_duplicates([1,2,3,1]))
    print(contains_duplicates([1,2,3,4]))
    test_is_anagram()
    print(two_sum_indices([2,7,11,15],9))
    test_max_profit()
    test_is_palindrome()


    

