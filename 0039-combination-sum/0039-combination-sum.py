class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        nums = candidates
        n = len(nums)

        res = []
        sol = []

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return

            if curr_sum > target or i>=n:
                return

            # pick
            sol.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            sol.pop()

            # dont pick

            backtrack(i + 1, curr_sum)

        backtrack(0, 0)

        return res
