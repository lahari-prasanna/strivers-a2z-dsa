# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# E 
# D E 
# C D E 
# B C D E 
# A B C D E

def pattern18(n):
    for i in range(n):
        for j in range(n-i-1,n):
            print(chr(ord('A')+j),end="")
            if j!=n-1:
                print(" ",end="")
        print()

n=int(input("Enter a number: "))
pattern18(n)

