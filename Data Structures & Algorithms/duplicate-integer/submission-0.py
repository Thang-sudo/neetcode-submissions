class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # iterate over the list
        # all numbers we have seen so far stored in a dictionary
        # if the next number is already in dictionary returns true
        # if we scan the whole array and still cant find, return false
        # We might need to scan the whole array, then the complexity would be O(n)
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = True
            else:
                return True
        return False

        