# Given an integer array nums, rotate the array to the left by one.
# Note: There is no need to return anything, just modify the given array.

def left_rotate_by_one(nums):
    n=len(nums)
    temp=nums[0]
    for i in range(1,n):
        nums[i-1]=nums[i]
    nums[n-1]=temp

nums=[-1,0,3,6]
left_rotate_by_one(nums)
print(nums)