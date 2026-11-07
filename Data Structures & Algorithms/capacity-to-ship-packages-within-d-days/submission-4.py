class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_cap = sum(weights)
        min_cap = max(weights)
        result = max_cap
        # Check if we can devivery all weights within the given days
        def canDeliver(cap: int) -> bool:
            # how much ship is carrying
            carry = 0
            # how many day the ship has delivered packages so far
            d_days = 1
            for w in weights:
                # the current capacity cant carry this weight
                if w > cap:
                    return False
                # try to add the weight to curent carried weight
                if carry + w > cap:
                    # the weight need to be carried in the next day
                    carry = w
                    d_days += 1
                # elif carry + w == cap:
                #     # adding the weight to the ship reached capacity
                #     carry = 0
                #     d_days += 1
                else:
                    # added the weight but we still have capacity to carry more
                    carry += w
                # if number delivery days we used so far exceed what allowed
                if d_days > days:
                    return False
            return True

        l, r = min_cap, max_cap
        while l < r:
            m = (l + r) // 2
            # if we can deliver with the current weight -> need to try with smaller cap
            if canDeliver(m):
                result = min(result, m)
                r = m
            # if we cant deliver with current weight -> need to try with bigger cap
            else:
                l = m + 1
        return result




                
        
        