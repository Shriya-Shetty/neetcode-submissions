class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dict1 = {}
        dict2 = {}

        for i in s1:
            dict1[i] = dict1.get(i, 0) + 1

        left = 0

        for right in range(len(s2)):

            # Add current character
            dict2[s2[right]] = dict2.get(s2[right], 0) + 1

            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):
                dict2[s2[left]] -= 1

                if dict2[s2[left]] == 0:
                    del dict2[s2[left]]

                left += 1

            # Check if frequencies are same
            if dict1 == dict2:
                return True

        return False