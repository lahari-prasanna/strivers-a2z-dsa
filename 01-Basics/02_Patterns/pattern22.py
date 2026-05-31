# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:


# 5 5 5 5 5 5 5 5 5 
# 5 4 4 4 4 4 4 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 2 1 2 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 4 4 4 4 4 4 5 
# 5 5 5 5 5 5 5 5 5

def pattern22(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top=i
            bottom=2*n-2-i
            right=2*n-2-j
            left=j
            print(n-min(top,bottom,right,left),end="")
            if j!=2*n-2:
                print(" ",end="")
        print()

n=int(input("Enter a number: "))
pattern22(n)