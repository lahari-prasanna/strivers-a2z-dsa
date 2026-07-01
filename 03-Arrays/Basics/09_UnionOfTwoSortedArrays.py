# Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.

# The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.

# def union_of_arrays(nums1,nums2):
#     res=set()
#     for num in nums1:           #O(n)
#         res.add(num)

#     for num in nums2:           #O(m)
#         res.add(num)

#     return sorted(res)          #O(klog k) k=n+m

#T.C: O((n+m) log (n+m)) S.C: O(n+m)

def union_of_arrays(nums1, nums2):
    i, j = 0, 0
    result = []

    while i < len(nums1) and j < len(nums2):

        if nums1[i] < nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1

        elif nums1[i] > nums2[j]:
            if not result or result[-1] != nums2[j]:
                result.append(nums2[j])
            j += 1

        else:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
            j += 1

    while i < len(nums1):
        if not result or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1

    while j < len(nums2):
        if not result or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

    return result

#T.C: O(n+m) S.C: O(n+m)
        


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
union=union_of_arrays(nums1,nums2)
print(union)




