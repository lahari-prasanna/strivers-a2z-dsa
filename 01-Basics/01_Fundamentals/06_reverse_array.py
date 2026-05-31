# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

def reverse_array(arr):
    start=0
    end=len(arr)-1
    while(start<end):
        #swap
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp

        #update
        start+=1
        end-=1

    return arr

reversed_array=reverse_array([1,2,3,4])
print(reversed_array)

