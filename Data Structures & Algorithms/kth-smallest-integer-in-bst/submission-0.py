# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = 0
        result = -1
        def inOrderTraversal(root: Optional[TreeNode]) -> None:
            nonlocal order, result
            if not root:
                return
            inOrderTraversal(root.left)
            order += 1
            if order == k:
                result = root.val
            inOrderTraversal(root.right)
        
        inOrderTraversal(root)
        return result
            



        