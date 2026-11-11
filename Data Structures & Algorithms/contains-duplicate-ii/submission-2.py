class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = right = 0
        window = set()
        while right < len(nums):
            while right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])
            right += 1
        return False
        