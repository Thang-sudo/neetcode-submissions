from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize prefix products and suffix products arrays
        # Iterate from left to right, for each i -> calculate the prefix product, meaning the products from 0 -> i - 1. No prefix -> 1. prefix[i] = nums[i - 1] * prefix[i - 1]
        # Iterate from right to left, for each i -> calculate the suffix product, meaning the prodcts from i + 1 -> n - 1. No suffix -> 1. suffix[i] = nums[i + 1] * suffix[i + 1]
        # Now we have 2 lists with the same number of elements
        # Iterate both lists take product of prefix[i] * suffix[i] -> results[i]
        prefix = []
        suffix = []
        results = []
        # calculate prefix
        for i in range(len(nums)):
            prefix_product = 1
            if i > 0:
                prefix_product = nums[i - 1] * prefix[i - 1]
            prefix.append(prefix_product)
        # calculate suffix
        j = -1
        for i in reversed(range(len(nums))):
            suffix_product = 1
            if i != (len(nums) - 1):
                suffix_product = nums[i + 1] * suffix[j]
            suffix.append(suffix_product)
            j += 1
        j = len(nums) - 1
        for i in range(len(nums)):
            results.append(prefix[i] * suffix[j])
            j -= 1
        return results


        