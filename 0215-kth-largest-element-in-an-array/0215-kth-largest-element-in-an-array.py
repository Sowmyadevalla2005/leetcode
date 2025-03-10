import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        return -nums[0]


        