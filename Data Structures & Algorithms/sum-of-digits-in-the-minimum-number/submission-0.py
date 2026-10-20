class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_number = min(nums)
        digit_sum = 0
        while min_number:
            digit_sum += min_number % 10
            min_number = min_number // 10
        return int(not (digit_sum % 2))
