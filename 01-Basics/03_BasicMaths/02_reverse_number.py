# You are given an integer n. Return the integer formed by placing the digits of n in reverse order

def reverse_number(n):
    reverse=0
    while(n!=0):
        digit=n%10
        reverse=reverse*10+digit
        n//=10

    return reverse

n=int(input("Enter a number: "))
print(reverse_number(n))
        