class Solution:
    def check(self, nums: List[int]) -> bool:
        s=sorted(nums)
        for i in range(len(nums)):
            if s==nums:
                return True
            e=s.pop(-1)
            s.insert(0,e)
        return False  
        