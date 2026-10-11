class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        combination = []
        def dfs():
            if len(combination) == len(nums):
                res.append(combination.copy())
                return
            # Take candidates[i] to the combination
            for num in nums:
                if num in combination:
                    continue
                combination.append(num)
                dfs()
                combination.pop()
        dfs()
        return res
