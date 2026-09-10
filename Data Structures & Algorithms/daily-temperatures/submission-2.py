from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = []  # stores indices
        
        for i in range(n):
            # While current temp is greater than the temp at stack top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                output[prev_index] = i - prev_index
            stack.append(i)
        
        return output
