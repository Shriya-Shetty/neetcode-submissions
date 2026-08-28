class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=[]
        for char in s:
            if "A"<=char<="Z" or "a"<=char<="z" or '0'<=char<='9':
                result.append(char.lower())
        print(result)
        return result==result[::-1]
        