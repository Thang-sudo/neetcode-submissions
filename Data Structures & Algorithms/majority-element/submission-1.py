class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # if it is the current res then counter + 1 else counter - 1
        # if count is 0, this is a new element then set res as this num
        res = count = 0
        for num in nums:
            if count == 0:
                res = num
            count += 1 if num == res else -1
        return res
        