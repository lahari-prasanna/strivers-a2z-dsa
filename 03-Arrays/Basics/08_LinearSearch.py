# Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1

def linearSearch(nums, target):
    for i in range(0,len(nums)):
        if nums[i]==target:
            return i
    return -1

nums = [2, 3, 4, 5, 3]
target = 3
idx=linearSearch(nums,target)
print(f"The smallet index of the target {target} is found at the index {idx}")