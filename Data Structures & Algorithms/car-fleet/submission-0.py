class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleets = []
        for car in cars:
            time = (target - car[0]) / car[1]
            if not fleets or (fleets and time > fleets[-1]):
                fleets.append(time)

        return len(fleets)