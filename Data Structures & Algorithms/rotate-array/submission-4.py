class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1, 2, 3, 4, 5, 6, 7, 8] k = 2 
        #[7, 2, 3, 4, 5, 6, 1, 8]
        #[7, 8, 3, 4, 5, 6, 1, 2]
        def reversal(i: int, j: int):
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
        n = len(nums)
        k %= n
        reversal(0, n - 1)
        reversal(0, k - 1)
        reversal(k, n - 1)
        

        
        