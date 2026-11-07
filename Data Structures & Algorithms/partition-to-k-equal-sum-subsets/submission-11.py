class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        # form k subsets with 0 sum
        subsets = [0] * k
        # if any path has sum bigger than this target, reject that path
        target_sum = sum(nums) // k
        for i in nums:
            if i > target_sum:
                return False
        # sort nums in descending order. If adding a number to subset exceed target_sum, reject that path
        nums.sort(reverse = True)
        def dfs(i: int) -> bool:
            # if no more number to add to the subset check if all subsets equal to the target sum
            # this is correct becase we always check if the other subsets smaller or equal to target_sum
            if i == len(nums):
                return True
            # Try to add the number to each subset
            for j in range(k):
                if j > 0 and subsets[j] == subsets[j - 1]:
                    continue
                subsets[j] += nums[i]
                # the number belongs to this subset if putting in the current subset has the sum of subset smaller and equal to the target_sum and subsequent numbers still have a place to put it into a subset
                if subsets[j] <= target_sum and dfs(i + 1):
                    return True
                subsets[j] -= nums[i]
                # We tried to add the element to an empty bucket -> there will be no bucket appropriate to put this number in
                if subsets[j] == 0:
                    return False
            return False
        return dfs(0)
            
            

        
        