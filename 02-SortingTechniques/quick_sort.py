# Given an array of integers called nums, sort the array in non-decreasing order using the quick sort algorithm and return the sorted array.
# A sorted array in non-decreasing order is an array where each element is greater than or equal to all preceding elements in the array.
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=pivot and i<=high-1):
            i+=1
        while(arr[j]>pivot and j>=low+1):
            j-=1
        if(i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[low]=arr[low],arr[j]
    return j

def qs(arr,low,high):
    if(low<high):
        partitionIdx=partition(arr,low,high)
        qs(arr,low,partitionIdx-1)
        qs(arr,partitionIdx+1,high)


def quick_sort(arr):
    qs(arr,0,len(arr)-1)
    return arr


arr=[3,4,1,7,9,2,2,6,5]
res=quick_sort(arr)
print(res)


#T.C: O(N log N)
#S.C: O(1)