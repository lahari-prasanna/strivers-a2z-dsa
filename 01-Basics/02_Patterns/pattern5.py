# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *****
# ****
# ***
# **
# *


def pattern5(n):
    for i in range(1,n+1):
        for  j in range(1,n+2-i):
            print("*",end="")
        print()

num=int(input("Enter a number: "))
pattern5(num)