class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,result, ans,i):
            if i==len(nums):
                result.append(ans[:])
                return
            
            ans.append(nums[i])
            backtrack(nums,result, ans,i+1)
            ans.pop()
            backtrack(nums,result, ans,i+1)
        
        result=[]
        ans=[]
        backtrack(nums,result, ans,0)

        return result
