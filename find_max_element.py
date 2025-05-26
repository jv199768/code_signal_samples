# Find the maximum element in a list without using max()

def find_max_element(lst):
    max_element = lst[0]  # Initialize with the first element
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

# Example usage
sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(find_max_element(sample_list))  # Output: 9
