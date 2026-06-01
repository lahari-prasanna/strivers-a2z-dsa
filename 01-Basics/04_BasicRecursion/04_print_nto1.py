# Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.

# You must not use any loops such as for, while, or do-while.
# The function should print each number on a separate line, in decreasing order from n to 1

def printNumbers(n):
    if n==0:
        return
    print(n)
    printNumbers(n-1)

n=int(input("Enter a number: "))
printNumbers(n)