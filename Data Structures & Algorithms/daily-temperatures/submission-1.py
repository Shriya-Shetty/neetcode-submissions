from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = []  # will store indices of warmer days

        for i in range(n-1, -1, -1):  # go backwards
            # Pop all days that are not warmer
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            # If stack not empty, next warmer day is at stack[-1]
            if stack:
                output[i] = stack[-1] - i
            # Push current day
            stack.append(i)

        return output
