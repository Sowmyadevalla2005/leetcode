class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        s={}
        for num in nums:
            if num in s:
                s[num]+=1
            else:
                s[num]=1
        max_freq=max(s.values())

        total_count=0
        for c in s.values():
            if c==max_freq:
                total_count+=c
        return total_count



        