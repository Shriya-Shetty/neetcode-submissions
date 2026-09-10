class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n=len(matrix[0])
        m=len(matrix)

        l=0
        r=n*m-1
        while(l<=r):
            mid=(l+r)//2
            row=mid//n
            col=mid%n
            val=matrix[row][col]
            if target>val:
                l=mid+1
            elif target<val:
                r=mid-1
            elif target==val:
                return True 
            
        return False
