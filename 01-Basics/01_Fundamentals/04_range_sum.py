# Given two integers low and high, return the sum of all integers from low to high inclusive.

def range_sum(low,high):
    sum=0
    for i in range(low,high+1):
        sum+=i
    return sum

total_sum=range_sum(1,10)
print(total_sum)