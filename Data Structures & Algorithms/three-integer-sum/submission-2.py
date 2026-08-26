class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort array in non-decreasing order
        # iterate i from 0 to n - 1
        # for each nums[i] find nums[j] + nums[k] == -nums[i]
        # nums=[-1,0,1,2,-1,-4]
        # sorted = [-4, -1, -1, 0, 1, 2]
        nums.sort()
        results = []
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while j < k:
                if nums[j] + nums[k] < nums[i] * -1:
                    j += 1
                elif nums[j] + nums[k] > nums[i] * -1:
                    k -= 1
                else:
                    results.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return results
        