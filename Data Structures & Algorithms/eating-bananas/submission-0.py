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



        