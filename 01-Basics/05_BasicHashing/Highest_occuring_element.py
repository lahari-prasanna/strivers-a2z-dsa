# Given an array nums of n integers, find the most frequent element in it i.e., the element that occurs the maximum number of times. If there are multiple elements that appear a maximum number of times, find the smallest of them.

def highest_occuring_element(arr):
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
        
    max_freq=max(freq.values())
    result=[]
    for key,value in freq.items():
        if value==max_freq:
            result.append(key)
    return min(result)

arr=[1,1,1,2,2,2,3,4,]
print(highest_occuring_element(arr))

