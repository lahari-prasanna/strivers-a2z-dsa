# Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.

def NumbersSum(n):
    if n==1:
        return n
    
    return n + NumbersSum(n-1)    

n=int(input("Enter a number: "))
print(NumbersSum(n))


#T.C: O(n)
#S.C: O(n)