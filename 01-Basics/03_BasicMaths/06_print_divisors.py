# You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.



# A number which completely divides another number is called it's divisor.

def print_divisors(n):
    small=[]
    large=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            small.append(i)
            if i!=n//i:
                large.append(n//i)
    return small+ large[::-1]

n=int(input("Enter a number: "))
print(print_divisors(n))
