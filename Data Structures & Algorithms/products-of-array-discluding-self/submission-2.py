from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize prefix products and suffix products arrays
        # Iterate from left to right, for each i -> calculate the prefix product, meaning the products from 0 -> i - 1. No prefix -> 1. prefix[i] = nums[i - 1] * prefix[i - 1]
        # Iterate from right to left, for each i -> calculate the suffix product, meaning the prodcts from i + 1 -> n - 1. No suffix -> 1. suffix[i] = nums[i + 1] * suffix[i + 1]
        # Now we have 2 lists with the same number of elements
        # Iterate both lists take product of prefix[i] * suffix[i] -> results[i]
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        results = [1] * n
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(n):
            results[i] = prefix[i] * suffix[i]
        return results


        