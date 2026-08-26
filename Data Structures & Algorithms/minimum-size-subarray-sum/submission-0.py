class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = 0
        n = len(nums)
        minLength = float("inf")
        currentSum = 0
        currentLength = 0
        left = right = 0
        while right < n:
            # Add number to window
            currentSum += nums[right]
            currentLength += 1
            while currentSum >= target:
                minLength = min(minLength, currentLength)
                currentSum -= nums[left]
                currentLength -= 1
                left += 1
            right += 1
        return 0 if minLength == float("inf") else minLength
        