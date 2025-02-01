class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s=[]
        for i in range(1,len(arr)+k+1):
            if i not in arr:
                s.append(i)
        return s[k-1]

        