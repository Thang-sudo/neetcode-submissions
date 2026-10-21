class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return False
            seen.add(n)
        return max(nums) - min(nums) == len(nums) - 1