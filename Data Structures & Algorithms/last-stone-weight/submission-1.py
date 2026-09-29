class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)
            remaining = abs(x - y)
            if remaining > 0:
                heapq.heappush(max_heap, -1 * remaining)
        return 0 if len(max_heap) == 0 else -1 * heapq.heappop(max_heap)
        