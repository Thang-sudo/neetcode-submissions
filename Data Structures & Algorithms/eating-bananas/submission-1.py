class Solution:
    def getTime(self, speed, piles):
        time = 0
        for i in piles:
            if i <= speed:
                time += 1
            else:
                time += math.ceil(i / speed)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The maximum speed that we should eat = max(piles)
        # Run binary search from 1 -> max(piles) to search for the best eating speed
        # If eating_time at speed x <= max time -> k = min(k,x) -> search speed in x - 1 for better result
        # If eating_time at speed x > max time -> search speed in x + 1 for time within the boundary
        lower, upper = 1, max(piles)
        k = upper
        while lower <= upper:
            middle = (lower + upper) // 2
            time_to_eat = self.getTime(middle, piles)
            if time_to_eat <= h:
                k = min(k, middle)
                upper = middle - 1
            else:
                lower = middle + 1
        return k



        