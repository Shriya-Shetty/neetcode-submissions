class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        left = 0
        result = 0

        for right in range(len(s)):
            # update frequency of current char
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # if window is invalid, shrink from left
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # update result with valid window size
            result = max(result, right - left + 1)

        return result
