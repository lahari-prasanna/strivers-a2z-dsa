# Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.

def bubble_sort(nums):
    n=len(nums)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                #swap
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
    return nums



nums=[2,50,15,64,36]
result=bubble_sort(nums)
print(result)