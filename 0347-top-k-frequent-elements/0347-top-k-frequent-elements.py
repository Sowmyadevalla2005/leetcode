from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        l=[]
        for key,v in counter.items():
            l.append((v,key))
        l.sort(reverse=True)
        s=[]
        for val,ele in l[:k]:
            s.append(ele)
        return s



        