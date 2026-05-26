# Given a digit d (0 to 9), find the sum of the first 50 positive integers (integers > 0) that end with digit d.

# A number ends with digit d if its last digit is d.

digit=int(input("Enter a number: "))

def sum_numbers(d):
    return 25+(2*d+490)

sum=sum_numbers(1)
print(sum)


#It forms AP and so used the formula n/2*(2a+(n-1)*d)