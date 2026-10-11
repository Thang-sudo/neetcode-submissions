class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        combination = []
        used = set()
        def dfs():
            # If we added all elements to the combination. Then we completed a permutation
            if len(combination) == len(nums):
                res.append(combination.copy())
                return
            # for each element in nums. If that element is not in the current position in combination then add it to combination.
            # then recursively add other elements for the next positions
            # if an element already used in a position in combination then skip it
            # After we get a permutation, pop an element in combination, so we can try other elements in that position
            for num in nums:
                # Check if a number has been placed anywhere in permutation
                if num in used:
                    continue
                combination.append(num)
                used.add(num)
                dfs()
                removed = combination.pop()
                used.remove(removed)
        dfs()
        return res
