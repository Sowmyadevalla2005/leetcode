class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def valid_anagram(dicia,dicib):
            for i in dicia:
                if i not in dicib:
                    return False
                    
                if dicia[i] != dicib[i]:
                    return False
            return True
        
        l = 0
        k = len(p)
        n = len(s)
        dicia = {}
        dicib = {}
        ans = []
        for i in range(k):
            if p[i] not in dicib:
                dicib[p[i]] = 1
            else:
                dicib[p[i]] += 1
                
        for r in range(n):
            ch = s[r]
            if ch not in dicia:
                dicia[ch] = 1
            else:
                dicia[ch] += 1
            
            if r-l == k:
                dicia[s[l]] -= 1
                if dicia[s[l]] == 0:
                    dicia.pop(s[l])
                l += 1

            if r-l+1 == k:  
                if valid_anagram(dicia,dicib):
                    ans.append(l)
        
        return ans