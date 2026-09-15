# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # The diamater of any node is max depth of left tree + max depth of right tree
        max_diameter = 0
        def findMaxDepth(root) -> int:
            nonlocal max_diameter
            if not root:
                return 0
            left_height = findMaxDepth(root.left)
            right_height = findMaxDepth(root.right)
            max_diameter = max(max_diameter, left_height + right_height)
            
            return 1 + max(left_height, right_height)
        findMaxDepth(root)
        return max_diameter
