# Given an array of integers nums, return the value of the largest element in the array
def find_largest(arr):
    max=arr[0]
    for num in arr:
        if num>max:
            max=num
    return max


arr=[3,3,6,1]
largest_element=find_largest(arr)
print(largest_element)


#T.C: O(N)
#S.C: O(1)