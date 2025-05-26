def permute(nums):
    def backtrack(first=0):
        if first == len(nums):
            result.append(nums[:])
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first] # Swap numbers
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first] # Swap them back to reset the state

    result = []
    backtrack()
    return result

print(permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
