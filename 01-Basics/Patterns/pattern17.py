# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

def pattern7(n):

    for i in range(1, n + 1):

        # Print spaces
        for s in range(n - i):
            print(" ", end="")

        # Single loop for alphabets
        total=2*i-1
        for j in range(total):

            if j < i:
                ch = chr(65 + j)
            else:
                ch = chr(65 + (total-1-j))

            print(ch, end="")

        print()

n=int(input("Enter a number: "))
pattern7(n)


        
