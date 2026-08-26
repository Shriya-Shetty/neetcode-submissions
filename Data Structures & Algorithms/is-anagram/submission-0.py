class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict={}
        dict1={}
        for i in s:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in t:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        return dict==dict1

        