# Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same.

# def move_zeroes_to_end(nums):
#     n=len(nums)
#     temp=list()
#     for i in range(0,n):
#         if nums[i]!=0:
#             temp.append(nums[i])

#     for i in range(0,len(temp)):
#         nums[i]=temp[i]

#     for i in range(len(temp),n):
#         nums[i]=0

#T.C: O(N) S.C: O(N)



def move_zeroes_to_end(nums):
    j=-1
    for i in range(0,len(nums)):
        if nums[i]==0:
            j=i
            break
    
    if j==-1: return 

    for i in range(j+1,len(nums)):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1

#T.C: O(N) S.C:O(1)

nums = [0, 1, 4, 9, 0, 2]
move_zeroes_to_end(nums)
print(nums)