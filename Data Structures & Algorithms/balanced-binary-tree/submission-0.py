# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMaxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.findMaxDepth(root.left), self.findMaxDepth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.findMaxDepth(root.left) - self.findMaxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
