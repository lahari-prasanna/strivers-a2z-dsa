# You are given an integer n. You need to check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.



# An armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

def is_armstrong(num):
    k=len(str(num))
    n=num
    sum=0

    while(n>0):
        digit=n%10
        sum+=digit**k
        n//=10

    return sum==num

num=int(input("Enter a number: "))
print(is_armstrong(num))