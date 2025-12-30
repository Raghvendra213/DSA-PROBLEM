# Second Largest Element 
def s_largest(nums):
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)

    # find largest
    for i in range(0, n):
        largest = max(largest, nums[i])

    # find second largest
    for i in range(0, n):
        if nums[i] > s_largest and nums[i] < largest:
            s_largest = nums[i]

    return s_largest


nums = [12, 45, 87, 55, 99, 23, 44, 89]
print(s_largest(nums))
