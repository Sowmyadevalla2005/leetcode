import heapq
class Solution(object):
    def minOperations(self, nums, k):
        cnt = 0
        heapq.heapify(nums)
        
        while True:


            if nums[0]>=k:
                break
            
            
            if len(nums) < 2:
                return cnt
            
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)

            new_value = (a * 2) + b
            heapq.heappush(nums,new_value)
            
            cnt += 1
        
        return cnt
