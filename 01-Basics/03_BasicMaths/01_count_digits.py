# You are given an integer n. You need to return the number of digits in the number.
# The number will have no leading zeroes, except when the number is 0 itself.

def count_no_of_digits(n):
    count=0
    while(n>0):
        count+=1
        n//=10
    return count

n=int(input("Enter a number: "))
print(count_no_of_digits(n))
