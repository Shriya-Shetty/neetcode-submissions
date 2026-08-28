from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        target = 0

        while nums:
            a = nums[0]
            i, j = 1, len(nums) - 1

            while i < j:
                s = a + nums[i] + nums[j]
                if s == target:
                    output.append([a, nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # skip duplicates for nums[i] and nums[j]
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif s < target:
                    i += 1
                else:
                    j -= 1

            # remove all duplicates of 'a' before next iteration
            nums = [x for x in nums if x != a]

        return output
