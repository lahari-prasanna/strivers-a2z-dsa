# You are given an integer n. You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.



# A prime number is a number which has no divisors except 1 and itself


def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


n=int(input("Enter a number: "))
print(is_prime(n))