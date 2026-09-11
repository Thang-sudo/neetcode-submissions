class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Create a decreasing queue of indices to keep track of the max value and order of elements in a window
        # always ensure that the value at queue(0) to be max value of window
        # if max value leaves window => pop left the first element in the queue => make sure that only the max value in the window
        # When adding a new value to the window, pop right all indices whose values smaller than the new value -> find the order of the new element in the window
        # since the window only moves right, it only matters if the current max still in the window and the next value is the new max value
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




        




        