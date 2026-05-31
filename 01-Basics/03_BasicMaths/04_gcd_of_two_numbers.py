# You are given two integers n1 and n2. You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.

# The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.

def find_gcd(n1,n2):
    while n2!=0:
        n1,n2=n2,n1%n2
    return n1

# def GCD( n1, n2):
#     for i in range(min(n1,n2),0,-1):
#         if n1%i==0 and n2%i==0:
#             return i



n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
print(find_gcd(n1,n2))

#Time complexity: O(log(min(a,b)))
#followed Euclidean algorithm
