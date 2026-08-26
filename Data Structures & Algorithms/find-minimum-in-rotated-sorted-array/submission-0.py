class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Rotated sorted array = two rising staircases with a cliff between them.
        # The minimum is the bottom of the cliff (where high run drops to low run)
        n = len(nums)
        left, right = 0, n - 1

        # left < right (NOT <=): we stop when the window collapses onto the cliff.
        # Pairs with "right = middle" below — <= here would spin forever at left==right.
        while left < right:
            middle = (left + right) // 2

            # Compare middle to the RIGHT edge — the right end is a stable reference
            # that always sits on the LOW staircase.
            if nums[right] < nums[middle]:
                # middle is on the HIGH run (above the cliff).
                # The min must be strictly to the right -> discard middle.
                left = middle + 1
            else:
                # middle is on the LOW run (at or past the cliff).
                # The min is HERE or to the left -> KEEP middle (it might be the bottom)
                right = middle
        # left == right: both pointers have landed on the cliff bottom.
        return nums[left]
        