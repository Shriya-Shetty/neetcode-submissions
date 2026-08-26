class Solution:
    
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in range(len(nums)):
            dict[nums[i]]=0
            
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            if dict[nums[i]]>1:
                return True
        return False
    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False

    '''

        


        