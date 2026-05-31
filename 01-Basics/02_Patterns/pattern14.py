# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# A
# AB
# ABC
# ABCD
# ABCDE

def pattern14(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(chr(65+j),end="")
        print()

n=int(input("Enter a number: "))
pattern14(n)