class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Remember this is an non-decreasing ordered array
        # we can have to pointers i, j start at index 0 and n - 1 of the array
        # scan from both sides to the middle
        # if nums[i] + nums[j] < target -> i++ => need bigger number
        # if nums[i] + nums[j] > target -> i++ => need smaller number
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return None