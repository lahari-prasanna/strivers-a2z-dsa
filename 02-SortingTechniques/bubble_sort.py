# Given an array of integers called nums,sort the array in non-decreasing order using the bubble sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.

def bubble_sort(nums):
    n=len(nums)
    for i in range(0,n-1):
        swap=0
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                #swap
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                swap=1
        print("count")
        if( not swap):
            return nums
    return nums



nums=[4,5,6,1,3,2]
result=bubble_sort(nums)
print(result)

#TC: worst and avg: O(n^2)  best: O(n)