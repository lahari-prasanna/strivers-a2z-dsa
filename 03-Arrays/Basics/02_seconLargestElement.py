# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

def secondLargest(arr):
    n=len(arr)
    largest=arr[0]
    sLargest=-1
    for i in range(0,n):
        if arr[i]>largest:
            sLargest=largest
            largest=arr[i]
        elif arr[i]<largest and arr[i]>sLargest:
            sLargest=arr[i]
    return sLargest





arr=[2,-7,4,-9,2,1,8,5]
sLargest=secondLargest(arr)
print(sLargest)