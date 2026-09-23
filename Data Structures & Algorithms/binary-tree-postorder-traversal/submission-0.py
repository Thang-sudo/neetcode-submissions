# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        results = []
        results.extend(self.postorderTraversal(root.left))
        results.extend(self.postorderTraversal(root.right))
        results.extend([root.val])

        return results