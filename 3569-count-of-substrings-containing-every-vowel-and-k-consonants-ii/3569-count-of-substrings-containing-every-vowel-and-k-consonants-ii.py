class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def helper(k):
            n=len(word)
            ans = 0
            l = 0
            v=Counter()
            c=0
            for r in range(n):
                if word[r] in 'aeiou':
                    v[word[r]]+=1
                else:
                    c+=1
                    
                while len(v)==5 and c>k:
                    if word[l] in "aeiou":
                        v[word[l]]-=1
                        if v[word[l]]==0:
                            del v[word[l]]
                    else:
                        c-=1
                    l+=1
                ans+=r-l+1
            return ans
        return helper(k)-helper(k-1)

                    