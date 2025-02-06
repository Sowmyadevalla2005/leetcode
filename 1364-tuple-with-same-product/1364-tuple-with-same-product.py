class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        s=sorted(list(set(nums)))
        cnt=0
        dict={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]

                if product in dict:
                    cnt+=dict[product]
                    dict[product]+=1
                else:
                    dict[product]=1
        return cnt*8
        