class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Step 1: Build frequency map for t
        need = {}
        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        have = {}
        required = len(need)   # number of unique chars we need
        formed = 0             # how many chars currently satisfied

        left = 0
        min_len = float("inf")
        res = ""

        # Step 2: Expand window with right pointer
        for right in range(len(s)):
            ch = s[right]
            have[ch] = have.get(ch, 0) + 1

            # If this char count matches what we need
            if ch in need and have[ch] == need[ch]:
                formed += 1

            # Step 3: Shrink window from left if valid
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]

                # Pop from left
                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

        return res
