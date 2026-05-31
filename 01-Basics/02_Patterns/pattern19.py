# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

def pattern19(n):
    #upper half
    for i in range(n):
        #stars
        for j in range(n-i):
            print("*",end="")

        #spaces
        for j in range(2*i):
            print(" ",end="")

        #stars
        for j in range(n-i):
            print("*",end="")

        print()
        
    #lowerhalf
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




n=int(input("Enter a number: "))
pattern19(n)

