# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

def pattern13(n):
    count=1
    for i in range(0,n):
        for j in range(0,i+1):
            print(count,end=" ")
            count+=1
            
        print()

n=int(input("Enter a number: "))
pattern13(n)
