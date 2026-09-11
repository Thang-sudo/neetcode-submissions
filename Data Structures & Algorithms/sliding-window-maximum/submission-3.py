class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, k - 1
        queue = deque()
        results = []

        for i in range(0, k):
            while len(queue) and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        results.append(nums[queue[0]])

        while right < len(nums) - 1:
            # Move the window
            if nums[left] == nums[queue[0]]:
                queue.popleft()
            left += 1
            right += 1
            # Add the new element to the decreasing index queue
            while len(queue) and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)
            results.append(nums[queue[0]])
        return results




        




        