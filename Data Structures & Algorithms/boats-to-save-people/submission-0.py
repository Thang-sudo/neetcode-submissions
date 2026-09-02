class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left = 0
        right = n - 1
        boats = 0
        print(people)
        while left <= right:
            if people[right] == limit or people[left] + people[right] > limit:
                right -= 1

            else:
                left += 1
                right -= 1
            boats += 1
        return boats
        
        