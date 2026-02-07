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

def test_binary_search():
    assert binary_search([1,3,5,7,9],9) == 4
    assert binary_search([1,3,5,7,9],11) == -1

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

def is_valid_parentheses(s):
    pile = []
    match = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    
    for char in s:
        if char in '{([':
            pile.append(char)
        else:
            if len(pile) == 0:
                return False
            top = pile[-1]

            if top != match[char]:
                return False
            
            pile.pop()

    return len(pile) == 0

def test_is_valid_parentheses():
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("()[]{}") == True
    assert is_valid_parentheses("(]") == False
    assert is_valid_parentheses("([)]") == False
    assert is_valid_parentheses("") == True


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def merge_sorted_lists(l1,l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
        
    if l1:
            current.next = l1
    else:
            current.next = l2
        
    return dummy.next

def test_merge_sorted_lists():
    a1 = ListNode(1)
    a2 = ListNode(2)
    a3 = ListNode(4)

    a1.next = a2
    a2.next = a3

    b1 = ListNode(1)
    b2 = ListNode(3)
    b3 = ListNode(4)

    b1.next = b2
    b2.next = b3

    merged = merge_sorted_lists(a1,b1)


    assert merged.val == 1
    assert merged.next.val == 1
    assert merged.next.next.val == 2
    assert merged.next.next.next.val == 3
    assert merged.next.next.next.next.val == 4
    assert merged.next.next.next.next.next.val == 4
    assert merged.next.next.next.next.next.next is None

def reverse_linked_list(head):
    if head == None:
        return None
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def test_reverse_linked_list():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)

    a.next = b
    b.next = c

    new_head = reverse_linked_list(a)
    
    assert new_head.val == 3
    assert new_head.next.val == 2
    assert new_head.next.next.val == 1
    assert new_head.next.next.next is None


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
    test_binary_search()
    test_is_valid_parentheses()
    print(is_valid_parentheses("(]"))
    test_reverse_linked_list()
    test_merge_sorted_lists()
    


    

