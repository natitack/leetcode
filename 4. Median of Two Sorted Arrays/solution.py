from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i= 0
        count = 0
        merged = []
        while i < len(nums1) and i < len(nums2):
            if nums1[i] >= nums2[i]:
                merged.append(nums2[i])
                merged.append(nums1[i])
            else:
                merged.append(nums1[i])
                merged.append(nums2[i])
            i += 1
            count +=2
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
            count +=1
        while i < len(nums2):
            merged.append(nums2[i])
            i += 1
            count +=1
        if count % 2 == 0:
            return (merged[count // 2 - 1] + merged[count // 2]) / 2
        else:
            return merged[count // 2]


