# Largest element of the array 

def largest_element(nums):
    largest = nums[0]
    n = len(nums)

    for i in range(0, n):
        # largest = max(largest, nums[i])
        if nums[i] > largest:
            largest = nums[i]
    return largest


nums = [99, 78, 56, 100, 34, 65, 32]
print(largest_element(nums))
