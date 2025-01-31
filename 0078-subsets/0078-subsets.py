class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s=[[]]
        for i in range(len(nums)):
            for j in range(len(s)):
                temp=s[j]+[nums[i]]
                s.append(temp)
        return s
        