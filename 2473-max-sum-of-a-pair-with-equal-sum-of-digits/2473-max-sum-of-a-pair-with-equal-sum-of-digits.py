class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        max_sum = -1

        for num in nums:
            sum_d = 0
            s = str(num)
            len_s = len(s) 
            for i in range(len_s): 
                sum_d += int(s[i])  

            if sum_d not in d:
                d[sum_d] = [num]
            else:
                d[sum_d].append(num)

        for value in d.values():
            if len(value) >= 2:
                value.sort(reverse=True) 
                max_sum = max(max_sum, value[0] + value[1])

        return max_sum
