class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            middle = (i + j) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                i = middle + 1 # Target larger then it must be on the right half
            else:
                j = middle - 1 # Target smaller then it must be on the left lelf
        return -1
        