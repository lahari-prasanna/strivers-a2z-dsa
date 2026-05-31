# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# 1
# 22
# 333
# 4444
# 55555

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="")
        print()

n=int(input("Enter a number: "))
pattern4(n)
