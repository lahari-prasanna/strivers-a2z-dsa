# Given a string s, return true if the string is palindrome, otherwise false.

# A string is called palindrome if it reads the same forward and backward.

def palindromeCheck(s):
    def helper(i,j):
        if i>=j:
            return True
        if s[i]!=s[j]:
            return False
        return helper(i+1,j-1)
    return helper(0,len(s)-1)


s=input("Enter any word: ")
print(palindromeCheck(s))