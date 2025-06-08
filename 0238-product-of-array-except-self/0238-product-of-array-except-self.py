class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[]
        t=1
        z_cnt = 0
        for i in nums:
            if i==0:
                z_cnt+=1
            else:
                t=t*i

        for i in range(0,len(nums)):
            if z_cnt>1:
                s.append(0)
            elif z_cnt==1:
                if nums[i]==0:
                    s.append(t)
                else:
                    s.append(0)
            else:
                s.append(t//nums[i])
        return s


        