# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

def isSorted(arr):
    n=len(arr)
    for i in range(1,n):
        if (arr[i]>arr[i-1]):
            pass
        else:
            return False
    return True

arr=[1,2,3,4,5]
print(isSorted(arr))

#T.C: O(n)
#S.C: O(1)