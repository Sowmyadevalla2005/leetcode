class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            b=target-nums[i]
            if b in mp:
                return [mp[b], i]
            mp[nums[i]] = i

        return []  