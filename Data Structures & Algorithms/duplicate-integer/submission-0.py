class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=1
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=0
            
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            if dict[nums[i]]>1:
                return True
        return False

        


        