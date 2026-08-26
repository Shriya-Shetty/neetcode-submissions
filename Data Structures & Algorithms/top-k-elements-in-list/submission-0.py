from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        result = []

        while k != 0:
            max_freq = float('-inf')
            max_num = None
            # loop over keys in dict
            for i in dict:
                if dict[i] > max_freq:
                    max_freq = dict[i]
                    max_num = i
            result.append(max_num)
            del dict[max_num]   # remove so next max can be found
            k -= 1

        return result
