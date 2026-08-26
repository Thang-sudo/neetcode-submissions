class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a seen dictionary where key is nums and value is indedx of nums
        # iterate over the nums list. For each, element i, check if target - i in seen dict. Returns the index of both i and target - i if seen.
        seen = {}
        for i in range(len(nums)):
            j = target - nums[i]
            if j in seen:
                return [seen[j], i]
            seen[nums[i]] = i
        return None
