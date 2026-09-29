class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-s for s in nums]
        heapq.heapify(max_heap)
        res = float('-inf')
        for i in range(k):
            res = -1 * heapq.heappop(max_heap)
        return res