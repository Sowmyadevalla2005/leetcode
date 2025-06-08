class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_prefix = [1]*len(nums)
        right_prefix = [1]*len(nums)

        s=[]
        

        for i in range(1,len(nums)):
            left_prefix[i]=left_prefix[i-1]*nums[i-1]
        
        

        for i in range(len(nums)-2,-1,-1):
            right_prefix[i]=right_prefix[i+1]*nums[i+1]
        
        

        for i in range(len(nums)):
            s.append(left_prefix[i]*right_prefix[i])
        return s
       




        