class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        start = 0
        maxlen = 0

        for i, ch in enumerate(s):
            if ch in dict and dict[ch] >= start:
                # move start just after the duplicate
                start = dict[ch] + 1
            dict[ch] = i
            maxlen = max(maxlen, i - start + 1)

        return maxlen
