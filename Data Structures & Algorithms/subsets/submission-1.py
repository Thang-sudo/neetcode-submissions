class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(i: int, subset: List[int]):
            # When we have no more elements to take or skip, then we just gonna
            if i == len(nums):
                self.res.append(subset.copy())
                return 
            # The case where we skip this element
            dfs(i + 1, subset)
            # The case where we take the element
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
        dfs(0, list())
        return self.res
            

        