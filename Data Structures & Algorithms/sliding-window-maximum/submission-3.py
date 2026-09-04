from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_element = float('-inf')
        left = 0
        slide = []
        result = []

        for right in range(len(nums)):
            ch = nums[right]
            slide.append(ch)

            # update max_element when new element enters
            if ch > max_element:
                max_element = ch

            if right - left + 1 >= k:
                # record current max
                result.append(max_element)

                # remove leftmost element
                removed = slide.pop(0)
                left += 1

                # if removed was the max, recompute manually
                if removed == max_element:
                    if slide:   # recompute only if window not empty
                        max_element = slide[0]
                        for val in slide:
                            if val > max_element:
                                max_element = val
                    else:
                        max_element = float('-inf')

        return result
