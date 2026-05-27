# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *****
# *****
# *****
# *****
# *****

def pattern1(n):
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
        print()

num=int(input("Enter a number: "))
pattern1(num)