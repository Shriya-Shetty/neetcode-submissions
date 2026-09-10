class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1   # minimum is in right half
            else:
                r = mid       # minimum is in left half (including mid)
        return nums[l]
