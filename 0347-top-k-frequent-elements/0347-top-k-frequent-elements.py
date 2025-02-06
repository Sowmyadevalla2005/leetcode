class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return [nums[0]]
        
        else:
            dict={}

            for i in nums:
                if i in dict:
                    dict[i]+=1
                else:
                    dict[i]=1

            sorted_counts=sorted(dict.items(),key=lambda item:item[1],reverse=True)

            ans=[]
            for i in range(k):
                ans.append(sorted_counts[i][0])
            return ans

        