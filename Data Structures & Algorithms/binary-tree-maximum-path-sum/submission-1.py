# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(root: Optional[TreeNode]):
            # For a given node, either the path passing the node is max value (meaning it's the node is the peak of a subtree). Or the node belongs to a branch of another subtree is part of the max path
            if not root:
                return 0
            left_max_path = max(dfs(root.left), 0)
            right_max_path = max(dfs(root.right), 0)
            # If the current node is the peak, does the path come through it is the max sum path
            self.res = max(self.res, root.val + left_max_path + right_max_path)
            # If the node is not the peak of the max sum path, then return it to calculate the sum of a longer path
            return root.val + max(left_max_path, right_max_path)
        dfs(root)
        return self.res
        