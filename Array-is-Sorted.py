# Check if the array is Sorted

def Sorted(nums):
    n = len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True
nums =[3,5,6,8,9,10,20,28,1]
print(Sorted(nums))