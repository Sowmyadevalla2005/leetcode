import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s=heapq.nlargest(k,nums)
        return s[-1]


        