# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

def pattern20(n):
    #upperhalf
    for i in range(n):
        #stars
        for j in range(i+1):
            print("*",end="")
        #spaces
        for j in range(2*(n-i-1)):
            print(" ",end="")
        #stars
        for j in range(i+1):
            print("*",end="")

        print()
    #lowerhalf
    for i in range(n-1):
        #stars
        for j in range(n-i-1):
            print("*",end="")
        #spaces
        for j in range(2*(i+1)):
            print(" ",end="")
        #stars
        for j in range(n-i-1):
            print("*",end="")
        print()


n=int(input("Enter a number: "))
pattern20(n)