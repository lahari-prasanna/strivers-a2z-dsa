# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def pattern10(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print()

    for i in range(1,n):
        for j in range(1,n-i+1):
            print("*",end="")
        print()

n=int(input("Enter a number: "))
pattern10(n)