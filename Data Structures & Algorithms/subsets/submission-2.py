class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.subset = []
        def dfs(i: int):
            # When we have no more elements to take or skip, then we just gonna
            if i == len(nums):
                self.res.append(self.subset.copy())
                return 
            # The case where we skip this element
            dfs(i + 1)
            # The case where we take the element
            self.subset.append(nums[i])
            dfs(i + 1)
            self.subset.pop()
        dfs(0)
        return self.res
            

        