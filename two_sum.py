def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target - num], i]
        hash_map[num] = i
    return []

# Test
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
