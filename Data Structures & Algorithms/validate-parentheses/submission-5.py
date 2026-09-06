class Solution:
    def isValid(self, s: str) -> bool:
        para={')': '(', '}': '{', ']': '['}
        stack=[]
        for i in s:
            if i in para and len(s)>1 and len(stack)>0:
                if stack[-1]==para[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

            
        return len(stack)==0


       
        


        
        