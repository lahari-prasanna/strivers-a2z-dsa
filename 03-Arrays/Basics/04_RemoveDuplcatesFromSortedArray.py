# Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once.

# Return the number of unique elements in the array.

# If the number of unique elements be k, then,

# Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
# The remaining elements, as well as the size of the array does not matter in terms of correctness

def remove_duplicates(arr):
    n=len(arr)
    i=0
    for j in range(1,n):
        if arr[i]==arr[j]:
            pass
        else:
            i+=1
            arr[i]=arr[j]
            
    return i+1



arr=[1,1,2,2,3]
unique_elements=remove_duplicates(arr)
print(unique_elements)