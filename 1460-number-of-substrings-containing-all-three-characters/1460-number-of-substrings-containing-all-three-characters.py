class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        count = {'a': 0, 'b': 0, 'c': 0}  
        total_substrings = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                total_substrings+=len(s)-right
                count[s[left]] -= 1
                left += 1
                
        return total_substrings