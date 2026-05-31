# You are given an integer n. You need to check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.



# A palindrome number is a number which reads the same both left to right and right to left.

def is_palindrome(n):
    original_number=n
    reversed_number=0
    while(n>0):
        digit=n%10
        reversed_number=reversed_number*10+digit
        n//=10
    if(original_number==reversed_number):
        return True
    return False

n=int(input("Enter a number: "))
print(is_palindrome(n))