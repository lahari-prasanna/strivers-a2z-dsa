# Given an array of integers, nums,sort the array in non-decreasing order using the merge sort algorithm. Return the sorted array.

# A sorted array in non-decreasing order is one in which each element is either greater than or equal to all the elements to its left in the array.

def merge(nums,low,mid,high):
    temp=[]
    left=low
    right=mid+1

    while(left <=mid and right<=high):
        if nums[left]<=nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1

    while(left<=mid):
        temp.append(nums[left])
        left+=1

    while(right<=high):
        temp.append(nums[right])
        right+=1
        
    for i in range(low,high+1):
        nums[i]=temp[i-low]

def ms(nums,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    ms(nums,low,mid)
    ms(nums,mid+1,high)
    merge(nums,low,mid,high)

def merge_sort(nums):
    ms(nums,0,len(nums)-1)
    return nums


nums=[4,2,1,6,9,3,8]
result=merge_sort(nums)
print(result)