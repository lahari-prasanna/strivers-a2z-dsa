# Given marks of a student, print on the screen:

# Grade A if marks >= 90
# Grade B if marks >= 70
# Grade C if marks >= 50
# Grade D if marks >= 35
# Fail, otherwise.


marks=int(input("Enter your marks: "))

if marks>=90:
    print("Grade A")
elif marks>=70 :
    print("Grade B")
elif marks>=50 and marks<70:
    print("Grade C")
elif marks>=35 and marks<50:
    print("Grade D")
else:
    print("Fail")

