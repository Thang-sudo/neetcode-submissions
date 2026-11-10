class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        car = []
        heapq.heapify(car)
        for num_pass, trip_begin, trip_end in trips:
            # Drop off passenger first
            while car and car[0][0] <= trip_begin:
                capacity += heapq.heappop(car)[1]
            # Do we have to pick up?
            if capacity < num_pass:
                return False
            capacity -= num_pass
            heapq.heappush(car, [trip_end, num_pass])     
        return True
