# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

# def reverse_array(i,j,arr):
#     if i>=j:
#         return
#     #swap
#     arr[i],arr[j]=arr[j],arr[i]
#     reverse_array(i+1,j-1,arr)

#     return arr

# arr=[1,2,3,4]
# i=0
# j=len(arr)-1
# print(reverse_array(i,j,arr))


def reverse_array(i,arr):
    if i>=n//2:
        return
    #swap
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    reverse_array(i+1,arr)

    return arr



arr=[1,2,3,4,5]
i=0
n=len(arr)
print(reverse_array(i,arr))