class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # max_heap = [-s for s in nums]
        # heapq.heapify(max_heap)
        # res = float('-inf')
        # for i in range(k):
        #     res = -1 * heapq.heappop(max_heap)
        # return res
        min_heap = nums[:k] # Get a list of first k characters
        heapq.heapify(min_heap) # The kth largest elemnt is the smallest value of first k largest elememts, which is the top value of this min heap
        # we need to make sure that the min_heap contains the first k largest value
        # comparing with the rest of elements of the list nums
        # if any elements larger than the top of min heap, then it should be replaced with that element
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num) # O(log k)
        return min_heap[0]
