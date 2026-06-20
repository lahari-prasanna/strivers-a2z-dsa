# Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.

# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        j=i
        while(nums[j]<nums[j-1]and j>0 ):
            #swap
            temp=nums[j]
            nums[j]=nums[j-1]
            nums[j-1]=temp
            j-=1
    return nums




nums=[2,4,7,3,1,9]
result=insertion_sort(nums)
print(result)


#T.C: Worst and avg: O(n^2) and Best case O(n)=> because no swaps happen the condition fails everytime