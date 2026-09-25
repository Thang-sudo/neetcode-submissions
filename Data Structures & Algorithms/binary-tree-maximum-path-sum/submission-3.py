# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(node):
            if not node:
                return 0
            # Calculate the max value of the left path
            left = max(dfs(node.left), 0) # don't add negative values to the max sum path
            right = max(dfs(node.right), 0) 

            # For any given node, try to make it a peak and see if the path pass through it has the max sum
            self.res = max(self.res, node.val + left + right)

            # in case the node is not the 'peak' of the max sum path. the max sum path only passes through either the left sub tree or right subtree from this node downward. Whichever path has better value. Then just return so upper node can calculate their path's sum
            return node.val + max(left, right)
        dfs(root)
        return self.res
        