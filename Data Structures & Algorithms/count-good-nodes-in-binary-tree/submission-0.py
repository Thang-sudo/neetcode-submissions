# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def dfs(root: TreeNode, maxval: int) -> None:
            nonlocal result
            if not root:
                return None

            if root.val >= maxval:
                maxval = root.val
                result += 1
            dfs(root.left, maxval)
            dfs(root.right, maxval)
        dfs(root, root.val)
        return result
