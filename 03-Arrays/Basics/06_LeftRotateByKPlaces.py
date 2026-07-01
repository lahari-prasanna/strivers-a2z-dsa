# Given an integer array nums and a non-negative integer k, rotate the array to the left by k steps.

#---Bruteforce approach----

# def left_rotate(arr,d):
#     n=len(arr)
#     d=d%n
#     temp=[]
#     for i in range(0,d):
#         temp.append(arr[i])
    
#     for i in range(d,n):
#         arr[i-d]=arr[i]
    
#     for i in range(n-d,n):
#         arr[i]=temp[i-(n-d)]

#T.C: O(n+d)
#S.C: O(d)



def reverse(i,j):
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

def left_rotate(arr,d):
    n=len(arr)
    d=d%n

    reverse(0,d-1)
    reverse(d,n-1)
    reverse(0,n-1)
    


arr=[4,2,8,9,4,0,1]
d=int(input("Enter the no of steps: "))
left_rotate(arr,d)
print(arr)


#T.C: O(n)
#S.C: O(1)