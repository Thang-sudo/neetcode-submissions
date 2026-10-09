class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.subset = []
        def dfs(i: int, current_sum: int):
            if current_sum > target:
                return
            if i == len(nums):
                if current_sum == target:
                    self.res.append(self.subset.copy())
                return
            # dont take the current element
            dfs(i + 1, current_sum)
            # take the current element
            self.subset.append(nums[i])
            dfs(i, current_sum + nums[i])
            # remove element from current subset once we're done with it
            self.subset.pop()
        dfs(0, 0)
        return self.res
