# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1

def pattern11(n):
    for i in range(0,n):
        for j in range(0,i+1):
            if (i+j)%2==0:
                print(1,end="")
            else:
                print(0,end="")

            if j!=i:
                print(" ",end="")
        print()

n=int(input("Enter a number: "))
pattern11(n)