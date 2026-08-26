class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # w = [0] * n
        # max_left = [0] * n
        # max_right = [0] * n
        # max_left[0] = height[0]
        # for i in range(1, n):
        #     max_left[i] = max(max_left[i - 1], height[i])
        # max_right[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     max_right[i] = max(max_right[i + 1], height[i])
        # for i in range(0, n):
        #     w[i] = min(max_right[i], max_left[i]) - height[i]
        # return sum(w)
        n = len(height)
        l = 0
        r = n - 1
        left_max = right_max = total = 0
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                total += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                total += right_max - height[r]
                r -= 1
        return total
            




