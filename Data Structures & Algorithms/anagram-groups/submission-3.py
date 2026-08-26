from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            # build frequency count manually
            freq = [0] * 26
            for ch in word:
                # map 'a'..'z' to 0..25
                idx = ord(ch) - ord('a')
                freq[idx] += 1
            
            key = tuple(freq)  # immutable key
            
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        
        return list(groups.values())
