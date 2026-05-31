# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# 12345
# 1234
# 123
# 12
# 1

def pattern6(n):
    for i in range(1,n+1):
        for j in range(1,n+2-i):
            print(j,end="")
        print()

n=int(input("Enter a number: "))
pattern6(n)