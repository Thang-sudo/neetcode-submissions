class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Reverse all, then reverse the first k, then reverse the last n-k
        def reversal(i: int, j: int):
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
        n = len(nums)
        # rotating n times result in the same original array
        # To save our time, just need to rotate k % n times
        k %= n 
        reversal(0, n - 1)
        reversal(0, k - 1)
        reversal(k, n - 1)
        

        
        