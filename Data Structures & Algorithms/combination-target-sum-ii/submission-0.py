class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []
        
        def dfs(i: int, current_sum: int):
            # We found the combination, add to result
            if current_sum == target:
                res.append(combination.copy())
                return 
            # Stop considering candidate if the current sum larger than the target
            # Or we out of candidate to consider
            if current_sum > target or i >= len(candidates):
                return

            else:
                # Keep considering candidate
                # Take case:
                combination.append(candidates[i])
                dfs(i + 1, current_sum + candidates[i])
                # Skip case:
                skipped_value = candidates[i]
                combination.pop()
                while i < len(candidates) - 1 and skipped_value == candidates[i + 1]:
                    i += 1
                dfs(i + 1, current_sum)
        dfs(0, 0)
        return res    

        