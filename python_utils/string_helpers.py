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

if __name__ == "__main__":
    print(char_frequency('hello'))
    print(is_anagram('anagram','nagaram'))
    print(is_anagram('rat','car'))
    print(contains_duplicates([1,2,3,1]))
    print(contains_duplicates([1,2,3,4]))
    test_is_anagram()
    print(two_sum_indices([2,7,11,15],9))


    

