import heapq

def find_k_largest(nums, k):
    return heapq.nlargest(k, nums)

# Test
print(find_k_largest([3, 2, 1, 5, 6, 4], 2))  # Output: [6, 5]
