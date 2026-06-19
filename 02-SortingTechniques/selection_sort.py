# Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.

def selection_sort(nums):
    for i in range(0,len(nums)-1):
        min_idx=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min_idx]:
                min_idx=j
        #swap
        temp=nums[min_idx]
        nums[min_idx]=nums[i]
        nums[i]=temp
    return nums

nums=[4,2,7,9,3,5]
result=selection_sort(nums)
print( result)


#Time Complexity : O(n^2)