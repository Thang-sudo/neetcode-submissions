class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        left, right = 0, k - 1
        curr_sum = 0
        points = 0
        # Calculate the sum of the first k elements
        for i in range(0, k):
            curr_sum += calories[i]
        while right < len(calories):
            if curr_sum > upper:
                points += 1
            elif curr_sum < lower:
                points -= 1
            
            if right == len(calories) - 1:
                break
            curr_sum -= calories[left]
            left += 1
            right += 1
            curr_sum += calories[right]
        return points
