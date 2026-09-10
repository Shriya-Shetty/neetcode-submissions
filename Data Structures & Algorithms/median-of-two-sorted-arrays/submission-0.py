from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        output = []
        
        # Merge both arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                output.append(nums1[i])
                i += 1
            else:
                output.append(nums2[j])
                j += 1
        
        # Add remaining elements
        while i < len(nums1):
            output.append(nums1[i])
            i += 1
        while j < len(nums2):
            output.append(nums2[j])
            j += 1
        
        # Find median
        n = len(output)
        if n % 2 == 1:
            return float(output[n // 2])
        else:
            return (output[n // 2 - 1] + output[n // 2]) / 2.0
