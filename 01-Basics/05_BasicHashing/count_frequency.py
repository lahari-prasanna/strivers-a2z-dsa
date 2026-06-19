# Given an array nums of size n which may contain duplicate elements.
# Rreturn a list of pairs where each pair contains a unique element from the array and its frequency in the array.
# You may return the result in any order, but each element must appear exactly once in the output.

def count_frequency(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    result=[]
    
    for key,value in freq.items():
        result.append([key,value])
    return result

arr=[1,2,2,1,3]
print(count_frequency(arr))