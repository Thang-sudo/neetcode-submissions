class Solution:
    def distanceFromRoot(self, x: int, y: int) -> int:
        return x ** 2 + y ** 2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # have a map to store distance where the key is the distance and the value is the actual point
        # iterate the list of points. For each point, calculate the distance
        # put the distance and point pair to the map distance -> map
        # heapify the map.keys()
        # heapq.heappop(heap) and add to the result list until len(results) == k
        # return results
        heap = []
        for point in points:
            x, y = point
            dist = self.distanceFromRoot(x, y)
            heapq.heappush(heap, (dist, x, y))
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            point = heapq.heappop(heap)
            dist, x, y = point
            res.append([x, y])
        return res





        