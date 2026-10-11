class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                # We out of candidate to consider
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            skipped = subset.pop()
            while i < len(nums) - 1 and skipped == nums[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res
