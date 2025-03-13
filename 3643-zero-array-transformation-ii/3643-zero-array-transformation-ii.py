class Solution(object):
    def minZeroArray(self, nums, queries):
        n = len(nums)
        q = len(queries)
        left, right = 0, q
        answer = -1

        def is_possible(k):
            diff = [0] * (n + 1)
        
            for j in range(k):
                l, r, val = queries[j]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val
            
            current_sum = 0
            for i in range(n):
                current_sum += diff[i]
                if nums[i] > current_sum:
                    return False
            return True

        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer if answer != -1 else -1
