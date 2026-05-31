# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

#     * 
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def pattern9(n):
    for i in range(1,n+1):
        #spaces
        for j in range(1,n-i+1):
            print(" ",end="")
        #stars
        for j in range(1,2*i):
            print("*",end="")
        print()

    for i in range(1,n+1):
        #spaces
        for j in range(1,i):
            print(" ",end="")

        #stars
        for j in range(1,2*n-(2*i-1)+1):
            print("*",end="")
        print()

n=int(input("Enter a number: "))
pattern9(n)
