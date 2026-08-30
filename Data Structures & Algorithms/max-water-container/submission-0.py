from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        
        while left < right:
            # width between the two lines
            width = right - left
            # height is limited by the shorter line
            area = min(heights[left], heights[right]) * width
            max_area = max(max_area, area)
            
            # move the pointer at the shorter line inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
