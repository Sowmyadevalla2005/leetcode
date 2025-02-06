class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        
        sorted_chars = sorted(d.items(), key=lambda item: item[1], reverse=True)

        res=""

        for i,val in sorted_chars:
            res+=i*val
        return res        
        