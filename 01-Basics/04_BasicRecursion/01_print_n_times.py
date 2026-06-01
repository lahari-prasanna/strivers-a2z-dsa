#Print something for n times using recursion


def print_n_times(n):
    if n==0:
        return

    print("Hello")
    print_n_times(n-1)

n=int(input("Enter a number: "))
print_n_times(n)

#T.C: O(n)
#S.C: O(n)