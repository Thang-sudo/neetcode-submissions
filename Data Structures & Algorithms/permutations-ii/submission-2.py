class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        result = []
        permutation = []
        used = [False] * len(nums)
        def dfs(i):
            # if we fill all positions of the permuation, add it to the result
            if i == len(nums):
                result.append(permutation[:])
                return
            # choose number to fill in the position i 
            for j in range(len(nums)):
                # If we already used this number, for this position, skip it
                if used[j]:
                    continue
                # Skip all duplicated numbers with the used number
                if j > 0 and nums[j] == nums[j - 1] and not used[j - 1]:
                    continue
                
                used[j] = True
                permutation.append(nums[j])
                dfs(i + 1)
                permutation.pop()
                used[j] = False
        dfs(0)
        return result